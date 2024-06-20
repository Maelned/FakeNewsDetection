import logging
import os
import pickle
import re

import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

logger = logging.getLogger()
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def get_data(csv_path):
    logger.info(f"Reading data from path : {csv_path}")
    data = pd.read_csv(csv_path, index_col=0)
    data = data.dropna(subset=['text'])
    return data

def preprocess_sentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    return ' '.join(token.lower() for token in sentence.split() if token.lower() not in stop_words)

def preprocess_text(text_data):
    preprocessed_text = []
    for sentence in text_data:
        preprocessed_text.append(preprocess_sentence(sentence))
    return preprocessed_text

def train(dest_path):
    """This function will perform the training of my fake news detection model
    """
    data = get_data("../data/data_news.csv")
    preprocessed_review = preprocess_text(data['text'].values) 
    data['text'] = preprocessed_review

    x_train, x_test, y_train, y_test = train_test_split(data['text'],  
                                                    data['label'],  
                                                    test_size=0.25)
    vectorization = TfidfVectorizer() 
    x_train = vectorization.fit_transform(x_train) 
    x_test = vectorization.transform(x_test)
    model = LogisticRegression() 
    model.fit(x_train, y_train) 

    logger.info(accuracy_score(y_train, model.predict(x_train))) 
    logger.info(accuracy_score(y_test, model.predict(x_test))) 

    with open(os.path.join(dest_path, "model.pkl"),'wb') as f:
        pickle.dump(model,f)

def main():
    
    dest_path = "../models"
    train(dest_path)


if __name__ == "__main__":
    main()