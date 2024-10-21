import sys
import os
import pytest
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_convert_temperature_celsius_to_fahrenheit(client):
    response = client.get('/convert/temperature?from=celsius&to=fahrenheit&value=0')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 32

def test_convert_temperature_fahrenheit_to_celsius(client):
    response = client.get('/convert/temperature?from=fahrenheit&to=celsius&value=32')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 0

def test_invalid_conversion(client):
    response = client.get('/convert/temperature?from=kelvin&to=celsius&value=0')
    assert response.status_code == 400

@patch('app.requests.get')
def test_convert_currency(mock_get, client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'rates': {'EUR': 0.85}, 
    }
    
    response = client.get('/convert/currency?from=USD&to=EUR&amount=10')
    json_data = response.get_json()
    
    assert response.status_code == 200
    assert 'result' in json_data
    assert json_data['result'] == 8.5  # 10 * 0.85
