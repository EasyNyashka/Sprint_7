import allure
import requests
from data import Url

class TestListOrderReturn:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order_return(self, create_and_cancel_order):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_LIST_ORDERS}')
        response_body = response.json()
        assert response.status_code == 200
        assert "orders" in response_body
