import pytest
import requests

@pytest.mark.integration
def test_integration():
    assert True

@pytest.mark.integration
def test_endpointHello():
    data = requests.get('http://localhost:5000/')
    assert data.text == "Welcome to the API!"

@pytest.mark.integration
def test_getData():
    data = requests.get('http://localhost:5000/api/data')
    assert data.json() == {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Software Developer'
    }
    assert data.status_code == 200
