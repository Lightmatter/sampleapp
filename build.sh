#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install --no-dev

npm install --no-fund
npm run build

python manage.py collectstatic --no-input
python manage.py migrate

while ! nc -z $(echo $DJANGO_AWS_S3_ENDPOINT_URL | echo "http://minio-pr-11.onrender.com" | cut -d "/" -f 3 -) 80; do echo 'Wait minio to startup...' && sleep 1; done;
sleep 5
poetry run python ./scripts/create_bucket.py
