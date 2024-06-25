First part is to train a ML model with a fixed dataset, once the ML model is convenient, use an API to collect news and classify them as fake news

Data link : https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification
API doc link : https://currentsapi.services/en/docs/
Ressources : https://arxiv.org/pdf/2201.07489


# My ML Project

## Overview

This is a simple machine learning project using Logistic regression with scikit-learn. It includes training and prediction scripts, along with Docker support for containerization.

The project can be divided into three main parts 

1. Training ML model
2. Retrieving News data from the API
3. Predict for each news if it is a fake news

## API Register

Sign up to the news API to get an access key to make get requests :

https://currentsapi.services/en/register

## AWS Connection

All the project use AWS storage with S3 and running with EC2. To do so you should create the bucket "fakenewsdetection" as it is detailed in the code python file __s3.py__. 
Moreover all the credentials are stored in the file __credentials.json__ file not uploaded on GitHub of course. Please find below an example of what should be inside the credential file.

```json
    {
    "acces_key": "AWS_ACCESS_KEY",
    "secret_acces_key": "AWS_SECRET_ACCESS_KEY",
    "api_key": "API_KEY"
    }
```

## Local Setup and Running
1. clone the git
2. unzip the data

1. Install [Poetry](https://python-poetry.org/).
2. Install dependencies:

    ```bash
    poetry install
    ```

3. Run the training script:

    ```bash
    poetry run python src/train.py
    ```

4. Run predictions:

    ```bash
    poetry run python src/predict.py
    ```

## Using Docker

1. Build the Docker image:

    ```bash
    docker build --build-arg ENTRYPOINT=fetch_news -t fake_news_detection .
    ```

2. Run the Docker container:

    ```bash
    docker-compose up -d
    ```

## Tests

Run tests with:

```bash
poetry run pytest tests/
