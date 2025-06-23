import pytest
import requests
from data import Url, Orders
from generators import generate_courier

@pytest.fixture
def courier_data():
    data = generate_courier()
    login = data['login']
    password = data['password']
    yield [data, login, password]
    login_data = {
        "login": login,
        "password": password
    }
    login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=login_data)
    courier_id = login_response.json()['id']
    requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER}/{courier_id}')


@pytest.fixture
def order_data():
    created_tracks = []
    def create(color):
        data = Orders.data_order.copy()
        data['color'] = color
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json=data)
        new_track = response.json()['track']
        created_tracks.append(new_track)
        return response
    yield create
    for track in created_tracks:
        requests.put(f'{Url.BASE_URL}{Url.CANCEL_ORDER}', params={'track': track})


