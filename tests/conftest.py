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
    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=login_data)
    response_body = login_response.json()
    assert login_response.status_code == 200 and 'id' in response_body
    courier_id = response_body['id']
    delete_response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}/{courier_id}')
    assert delete_response.status_code == 200, "Не удалось удалить тестового курьера"
