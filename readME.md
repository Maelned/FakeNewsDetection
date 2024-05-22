First part is to train a ML model with a fixed dataset, once the ML model is convenient, use an API to collect news and classify them as fake news

Data link : https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification
API doc link : https://newsapi.org/docs/get-started
Ressources : https://arxiv.org/pdf/2201.07489


# My ML Project

## Overview

This is a simple machine learning project using linear regression with scikit-learn. It includes training and prediction scripts, along with Docker support for containerization.

## Setup
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

## Docker

1. Build the Docker image:

    ```bash
    docker build -t my_ml_project .
    ```

2. Run the Docker container:

    ```bash
    docker run --rm my_ml_project
    ```

## Tests

Run tests with:

```bash
poetry run pytest tests/
