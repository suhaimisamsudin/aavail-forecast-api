# test endpoint - 26.03.2026 Suhaimi
# not fully working. need to debug further

import pytest
from app.api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_train(client):
    rv = client.post('/train')
    assert rv.status_code == 200
    assert b"success" in rv.data

def test_predict(client):
    rv = client.get('/predict?country=US&date=2026-04-01')
    assert rv.status_code == 200


