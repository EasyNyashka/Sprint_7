import pytest

import allure
import requests
from data import Url, Users
from generators import generate_courier

class TestLoginCourier:

    courier_data = generate_courier()

    @allure.title('Успешная авторизация курьера возвращает id, если передать все обязательные поля')
    def test_positive_login_courier(self):
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=TestLoginCourier.courier_data)
        login_data = {
            "login": TestLoginCourier.courier_data["login"],
            "password": TestLoginCourier.courier_data["password"]
        }
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json = login_data)
        response_body = login_response.json()
        assert login_response.status_code == 200 and 'id' in response_body

    @pytest.mark.parametrize('false_data_courier', [Users.false_login_data, Users.false_password_data])
    @allure.title('Система вернёт ошибку, если неправильно указать логин или пароль')
    def test_false_data_courier(self, false_data_courier):
        response_body = '{"message": "Учетная запись не найдена"}'
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=TestLoginCourier.courier_data)
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', json=false_data_courier)
        assert login_response.status_code == 404 and login_response.text == response_body


    @pytest.mark.parametrize('not_data_courier', [Users.not_login_data, Users.not_password_data])
    @allure.title('Система вернёт ошибку, если не указать логин или пароль')
    def test_not_all_data_courier(self, not_data_courier):
        response_body = '{"message":"Недостаточно данных для входа"}'
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=TestLoginCourier.courier_data)
        login_response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER}', data=not_data_courier)
        assert login_response.status_code == 400 and login_response.text == response_body