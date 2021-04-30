from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3BotoStorage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.MEDIA_LOCATIONs