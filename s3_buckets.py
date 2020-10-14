## Uplaoding to S3
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

#### Reading & excel or csv directly into python

import io
import boto3
import pandas as pd

#s3 client & bucket name
S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
S3_SECRET_KEY = os.environ['S3_SECRET_KEY']
s3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name = 'eu-central-1')
BUCKET = "sa-sd-dl"
item = 'INPUT/Sales/UR_USA.xls'
obj = s3.get_object(Bucket= BUCKET, Key=item)

### CSV
#df = pd.read_csv(obj['Body'])
### Excel
df = pd.read_excel(io.BytesIO(obj['Body'].read()))