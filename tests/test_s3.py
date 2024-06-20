import json
import os

import boto3
from moto import mock_s3

from src.s3 import retrieve_model, retrieve_news_bucket, upload_model, upload_to_s3

with open('credentials.json', 'r') as file:
    data = json.load(file)

AWS_ACCESS_KEY_ID = data.get("acces_key")
AWS_SECRET_ACCESS_KEY = data.get("secret_acces_key")
AWS_BUCKET_NAME = 'fakenewsbucket'

def test_retrieve_news_bucket():
    retrieve_news_bucket(AWS_BUCKET_NAME, "news_data_2024-06-05.json", "./tmp")
    assert os.path.exists('model.pkl')

@mock_s3
def test_upload():
    s3 = boto3.client('s3', region_name='eu-west-1')
    bucket_name = 'test-bucket'
    s3.create_bucket(Bucket=bucket_name)

    response = s3.list_buckets()
    assert bucket_name in [bucket['Name'] for bucket in response['Buckets']]

    s3.put_object(Bucket=bucket_name, Key='test.txt', Body=b'test file.')
    response = s3.list_objects_v2(Bucket=bucket_name)
    assert 'test.txt' in [obj['Key'] for obj in response.get('Contents', [])]

    response = s3.get_object(Bucket=bucket_name, Key='test.txt')
    content = response['Body'].read().decode('utf-8')
    assert content == 'test file.'

def test_retrieve_model():
    retrieve_model(AWS_BUCKET_NAME, model_name="model.pkl", dest_path="./tmp")
    assert os.path.exists('model.pkl')
