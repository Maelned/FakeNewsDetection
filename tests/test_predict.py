from src.predict import predict

def test_predict():
    test_data = 0 #TBD add data to test
    predictions = predict(test_data)
    assert len(predictions) == len(test_data)