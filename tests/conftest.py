import pytest
import requests
from data import Url
from generators import generate_courier

@pytest.fixture
def generate_courier_data():
    courier_data = generate_courier()
    login = courier_data['login']
    password = courier_data['password']
    yield [courier_data, login, password]
    login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json={"login": courier_data["login"], "password": courier_data["password"]})
    courier_id = login_response.json()["id"]
    delete_response = requests.delete(f'{Url.BASE_URL}{Url.LOGIN_COURIER}{courier_id}', json=courier_id)
    assert delete_response.status_code == 200
