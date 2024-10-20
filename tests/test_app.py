import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_convert_temperature_celsius_to_fahrenheit(client):
    # Testa a conversão de 0 graus Celsius para Fahrenheit
    response = client.get('/convert/temperature?from=celsius&to=fahrenheit&value=0')
    json_data = response.get_json()
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida
    assert json_data['result'] == 32  # Verifica se o resultado está correto

def test_convert_temperature_fahrenheit_to_celsius(client):
    # Testa a conversão de 32 graus Fahrenheit para Celsius
    response = client.get('/convert/temperature?from=fahrenheit&to=celsius&value=32')
    json_data = response.get_json()
    assert response.status_code == 200 
    assert json_data['result'] == 0  

def test_invalid_conversion(client):
    # Testa a conversão de uma unidade não suportada (kelvin) para Celsius
    response = client.get('/convert/temperature?from=kelvin&to=celsius&value=0')
    assert response.status_code == 400

@patch('app.requests.get')
def test_convert_currency(mock_get, client):
    # Testa a conversão de 10 dólares para euros, simulando a resposta da API de câmbio
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'rates': {'EUR': 0.85}, 
        'provider': '...',
    }
    
    response = client.get('/convert/currency?from=USD&to=EUR&amount=10')
    json_data = response.get_json()
    
    assert response.status_code == 200