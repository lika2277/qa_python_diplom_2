import pytest
import allure

@allure.suite('Получение заказов конкретного пользователя')
@pytest.mark.usefixtures('register_class')
class TestOrderGet:
    @allure.title('Авторизованный пользователь')
    def test_order_get_authorized(self, order):
        response = order.get_order(self.headers)
        data = response.json()
        assert (response.status_code == 200
                and data.get('success')
                and data.get('orders') is not None)

    @allure.title('Неавторизованный пользователь')
    def test_order_get_unauthorized(self, order):
        response = order.get_order()
        data = response.json()
        assert (response.status_code == 401
                and not data.get('success')
                and data.get('message') == 'You should be authorised')