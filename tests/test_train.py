import os

from src.train_model import train_model


def test_train_model():
    dest_path = "tests_data"
    train_model(dest_path)
    assert os.path.exists(os.path.join(dest_path,'model.pkl'))
