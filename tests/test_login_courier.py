import pytest
import allure
import requests
from data import Url, Users

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера возвращает id, если передать все обязательные поля')
    def test_positive_login_courier(self, courier_data):
        data, login, password = courier_data
        create_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        assert create_response.status_code == 201
        login_data = {
            "login": login,
            "password": password
        }
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=login_data)
        assert login_response.status_code == 200
        assert 'id' in login_response.json()

    @pytest.mark.parametrize('false_data_courier', [Users.false_login_data, Users.false_password_data])
    @allure.title('Система вернёт ошибку, если неправильно указать логин или пароль')
    def test_false_data_courier(self, courier_data, false_data_courier):
        data, login, password = courier_data
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=false_data_courier)
        assert login_response.status_code == 404
        assert login_response.json() == {"message": "Учетная запись не найдена"}


    @pytest.mark.parametrize('not_data_courier', [Users.not_login_data, Users.not_password_data])
    @allure.title('Система вернёт ошибку, если не указать логин или пароль')
    def test_not_all_data_courier(self, courier_data, not_data_courier):
        data, login, password = courier_data
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=not_data_courier)
        assert login_response.status_code == 400
        assert login_response.json() == {"message": "Недостаточно данных для входа"}