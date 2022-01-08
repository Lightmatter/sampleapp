import boto3
from botocore.client import Config
from os import environ as env

aws_access_key_id = env["DJANGO_AWS_ACCESS_KEY_ID"]
aws_secret_access_key = env["DJANGO_AWS_SECRET_ACCESS_KEY"]
endpoint_url = env["DJANGO_AWS_S3_ENDPOINT_URL"]
bucketname = env["DJANGO_AWS_STORAGE_BUCKET_NAME"]

source_s3 = boto3.resource(
    "s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)


def create_bucket():
    source_s3.create_bucket(bucketname)


if __name__ == "__main__":
    create_bucket()
