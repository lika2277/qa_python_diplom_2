import requests
import allure
from data.endpoints import endpoints

class Order:
    @staticmethod
    @allure.step('Создание заказа')
    def order(data=None, headers=None):
        return requests.post(endpoints.get('orders'), data=data, headers=headers)

    @staticmethod
    @allure.step('Получение заказов')
    def get_order(headers=None):
        return requests.get(endpoints.get('orders'), headers=headers)