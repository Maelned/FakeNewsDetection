import json
import logging
from datetime import datetime, timedelta

import requests

from s3 import upload_to_s3

logger = logging.getLogger()

with open('credentials.json', 'r') as file:
    data = json.load(file)

NEWS_API_KEY = data.get("api_key")
AWS_BUCKET_NAME = 'fakenewsbucket'


def fetch_news(api_key):
    url = "https://api.currentsapi.services/v1/latest-news"
    params = {
        "language" : "en",
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching news:", response.text)
        return None


def main():
    yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    news_data = fetch_news(NEWS_API_KEY)
    if news_data:
        file_name = f"news_data_{yesterday}.json"
        news_json = json.dumps(news_data)
        upload_to_s3(news_json, AWS_BUCKET_NAME, file_name)
        
        logger.info("News data uploaded successfully to AWS S3.")
    else:
        logger.error("Failed to fetch news data.")

if __name__ == "__main__":
    main()