import json
import logging
import os
from datetime import datetime, timedelta

from sklearn.feature_extraction.text import TfidfVectorizer

from s3 import retrieve_model, retrieve_news_bucket
from train_model import preprocess_text

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
logger = logging.getLogger()

def predict(date = None):
    if not date:
        date = yesterday
    bucket_name = 'fakenewsbucket'
    file_name = f"news_data_{yesterday}.json"
    dest_path = '../tmp'
    retrieve_news_bucket(bucket_name=bucket_name, file_name=file_name, dest_path=dest_path)
    file_path = os.path.join(dest_path, file_name)

    with open(file_path, 'r') as file:
        data = json.load(file)

    model = retrieve_model(dest_path=dest_path)
    news_descriptions = []
    for news  in data:
        proprocessed_text = preprocess_text(news['description'])
        news_descriptions.append(proprocessed_text)
    vectorization = TfidfVectorizer()
    news_descriptions = vectorization(news_descriptions)
    pred = model.predict(news_descriptions)

    
    print(pred)

def main():
    predict()

if __name__ == "__main__":
    main()