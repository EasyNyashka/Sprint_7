import pytest
import allure
import requests
from data import Url
from generators import generate_courier, generate_courier_no_password, generate_courier_no_login

class TestCreateCourier:

    @allure.title('Курьера можно создать, передав в ручку все обязательные поля')
    def test_create_courier(self):
        self.courier_data = generate_courier()
        response_body = '{"ok":true}'
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=self.courier_data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_courier_twice(self):
        courier_twice_data = generate_courier()
        response_body = '{"message": "Этот логин уже используется"}'
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=courier_twice_data)
        assert response.status_code == 201
        twice_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=courier_twice_data)
        assert twice_response.status_code == 409 and twice_response.text == response_body

    @pytest.mark.parametrize('courier_incomplete_data', [generate_courier_no_password, generate_courier_no_login])
    @allure.title('Если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_data_invalid(self, courier_incomplete_data):
        incomplete_data = courier_incomplete_data()
        response_body = '{"message": "Недостаточно данных для создания учетной записи"}'
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=incomplete_data)
        assert response.status_code == 400 and response.text == response_body