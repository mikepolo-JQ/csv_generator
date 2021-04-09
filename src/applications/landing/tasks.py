import boto3
from celery import shared_task
from django.conf import settings


@shared_task
def celery_file_download(filename):
    BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
    path = "D:/downAWS/"
    filepath = "media/" + filename

    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    s3.download_file(BUCKET_NAME, filepath, path + filename)
