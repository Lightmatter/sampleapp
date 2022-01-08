import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from os import environ as env

aws_access_key_id = env["DJANGO_AWS_ACCESS_KEY_ID"]
aws_secret_access_key = env["DJANGO_AWS_SECRET_ACCESS_KEY"]
endpoint_url = env["DJANGO_AWS_S3_ENDPOINT_URL"]
bucketname = env["DJANGO_AWS_STORAGE_BUCKET_NAME"]
api_port = ":9000"

source_s3 = boto3.client(
    "s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)


def create_bucket():
    try:
        source_s3.head_bucket(Bucket=bucketname)
        print(f"bucket {bucketname} exists!")
    except ClientError:
        print(f"creating bucket {bucketname}")
        try:
            source_s3.create_bucket(Bucket=bucketname)
        except ClientError as e:
            print("Unable to contact minio")
            print(e)


if __name__ == "__main__":
    create_bucket()
