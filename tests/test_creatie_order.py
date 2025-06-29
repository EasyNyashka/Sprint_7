import pytest
import allure

class TestCreateOrder:

    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GREY"],
        [""],
        ["BLACK", "GREY"]
    ])
    @allure.title('Создание заказа (цвет: {color})')
    def test_create_order(self, order_data, color):
        response = order_data(color)
        assert response.status_code == 201
        assert 'track' in response.text

