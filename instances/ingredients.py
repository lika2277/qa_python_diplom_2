import requests
import allure
import random
from data.endpoints import endpoints

class Ingredients:
    @allure.step('Получить список ингредиентов')
    def get_list(self):
        response = requests.get(endpoints.get('ingredients'))
        return response.json().get('data')

    @allure.step('Получить хеши ингредиентов')
    def get_random_hashes(self, length=3):
        return (random.choice(list(map(lambda ingredient: ingredient.get('_id'), self.get_list()))) for i in range(length))