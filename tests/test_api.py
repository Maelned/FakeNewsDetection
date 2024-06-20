import json

from src.news_api import fetch_news

with open('credentials.json', 'r') as file:
    data = json.load(file)

NEWS_API_KEY = data.get("api_key")


def test_train_model():
    news = fetch_news(NEWS_API_KEY)
    assert len(news) > 0
