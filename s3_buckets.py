########################################################################
# single function module for writing files directly to s3 without saving
########################################################################

#Standard library imports
import os

# Third party imports
import boto3
from io import StringIO


# AWS Credentials
S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
S3_SECRET_KEY = os.environ['S3_SECRET_KEY']
#S3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name = 'eu-central-1')
BUCKET = "sa-sd-dl"

def write_to_s3(df, key):
    """ Takes a pandas df as input & writes this use a StringIO buffer to write this
        directly to our s3 bucket. The df is saved in csv format and is saved using 
        the prescribed object key
        
        params: df = pandas df containing our simulation values (low or high), key = filename
        """
    
    csv_buffer = StringIO()
    #Write df to buffer
    df.to_csv(csv_buffer, sep=';', index=False)
    
    s3_resource = boto3.resource("s3", aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name = 'eu-central-1')
    
    #write buffer to s3
    s3_resource.Object(BUCKET, key).put(Body=csv_buffer.getvalue())
    print('Simulation: ' + key + ' written to S3') 


############### Uplaoding to S3
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

files = ['UR_USA.xls', 'Consumer_confidence.xls', 'US_GDP.xls', 'online_retail_sales.csv']

#s3 client & bucket name
S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
S3_SECRET_KEY = os.environ['S3_SECRET_KEY']

def get_s3_files():
    res = {}
    s3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name = 'eu-central-1')
    BUCKET = "sa-sd-dl"
    key = 'INPUT/Sales/'
    for f in files:
        path = key + f
        print(path)
        obj = s3.get_object(Bucket= BUCKET, Key=path)
        if (path[-3:] == "xls"):
            df = pd.read_excel(io.BytesIO(obj['Body'].read()))
        else:
            df = pd.read_csv(obj['Body'], sep=';')
        res[f] = df

