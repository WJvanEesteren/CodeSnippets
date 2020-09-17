import boto3
import os

KEY = os.environ['AWS_KEY']
SECRET_KEY = os.environ['AWS_SECRET_KEY']
REGION = os.environ['AWS_REGION']
BUCKET_NAME = 'gemeente-rotterdam-ai'

data = open('headshot.jpg', 'rb')

s3 = boto3.resource('s3', aws_access_key_id = KEY, aws_secret_access_key = SECRET_KEY)

s3.Bucket(BUCKET_NAME).put_object(Key='test.jpg', Body = data)

print('Done')