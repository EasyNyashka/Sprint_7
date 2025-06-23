import pytest
import allure
import requests
from data import Url
from generators import generate_courier_not_password, generate_courier_not_login

class TestCreateCourier:

    @allure.title('Курьера можно создать, передав в ручку все обязательные поля')
    def test_create_courier(self, courier_data):
        data, login, password = courier_data
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_courier_twice(self, courier_data):
        data, login, password = courier_data
        response1 = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        assert response1.status_code == 201
        response2 = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=data)
        assert response2.status_code == 409
        assert response2.json() == {"message": "Этот логин уже используется"}

    @pytest.mark.parametrize('courier_incomplete_data', [generate_courier_not_password, generate_courier_not_login])
    @allure.title('Если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_data_invalid(self, courier_incomplete_data):
        incomplete_data = courier_incomplete_data()
        expected_response = {"message": "Недостаточно данных для создания учетной записи"}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=incomplete_data)
        assert response.status_code == 400
        assert response.json() == expected_response