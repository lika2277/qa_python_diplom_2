import pytest
import allure

@allure.suite('Создание заказа')
@pytest.mark.usefixtures('register_class')
class TestOrderCreate:
    @allure.title('С авторизацией и с ингредиентами')
    def test_order_create_authorized(self, order, ingredients):
        response = order.order({'ingredients': ingredients}, self.headers)
        data = response.json()
        assert (response.status_code == 200
                and data.get('success')
                and data.get('order').get('ingredients') is not None)

    @allure.title('Без авторизации')
    def test_order_create_not_authorized(self, order, ingredients):
        response = order.order({'ingredients': ingredients})
        data = response.json()
        assert (response.status_code == 200
                and data.get('success')
                and data.get('order').get('ingredients') is None)

    @allure.title('Без ингредиентов')
    def test_order_create_without_ingredients(self, order):
        response = order.order({'ingredients': []}, self.headers)
        data = response.json()
        assert (response.status_code == 400
                and not data.get('success')
                and data.get('message') == 'Ingredient ids must be provided')

    @allure.title('С неверным хешем ингредиентов')
    def test_order_create_wrong_ingredient_hash(self, order, ingredients):
        wrong_ingredients = list(ingredients).append('xxxxxxxxxxxxxx')
        response = order.order({'ingredients': wrong_ingredients}, self.headers)
        data = response.json()
        assert (response.status_code == 400
                and not data.get('success')
                and data.get('message') == 'Ingredient ids must be provided')
