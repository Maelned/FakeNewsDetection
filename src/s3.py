
import json
import os
import pickle
from datetime import datetime, timedelta

import boto3
import requests

with open('credentials.json', 'r') as file:
    data = json.load(file)

AWS_ACCESS_KEY_ID = data.get("acces_key")
AWS_SECRET_ACCESS_KEY = data.get("secret_acces_key")
AWS_BUCKET_NAME = 'fakenewsbucket'

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

def retrieve_news_bucket(bucket_name, file_name, dest_path):
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key= AWS_SECRET_ACCESS_KEY, 
                      region_name="eu-north-1"
                      )
    s3.download_file(bucket_name, file_name, os.path.join(dest_path, file_name))

def upload_to_s3(data, bucket_name, file_name):
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key= AWS_SECRET_ACCESS_KEY, 
                      region_name="eu-north-1"
                      )
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)

def upload_model(bucket_name, model_name):
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key= AWS_SECRET_ACCESS_KEY, 
                      region_name="eu-north-1"
                      )
    model_path = f"../models/{model_name}"
    s3.upload_file(model_path, bucket_name, model_name)

def retrieve_model(bucket_name, model_name, dest_path):
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key= AWS_SECRET_ACCESS_KEY, 
                      region_name="eu-north-1"
                      )
    model_path = os.path.join(dest_path, model_name)
    s3.download_file(bucket_name, model_name, model_path)
    return pickle.load(model_path)




