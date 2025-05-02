import allure
import requests
import random
import string
from data.endpoints import endpoints

class User:
    @staticmethod
    @allure.step('Генерация нового пользователя')
    def generate():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        def generate_random_email(length):
            name = generate_random_string(length)
            domain = generate_random_string(length)
            return f'{name}@{domain[0:length-2]}.{domain[length-2:]}'
        return {
            "email": generate_random_email(5),
            "password": generate_random_string(10),
            "name": generate_random_string(10)
        }

    @staticmethod
    @allure.step('Создание пользовтеля')
    def register(payload=None):
        if not payload:
            raise Exception('Данные пользователя для создания не переданы')
        return requests.post(endpoints.get('register'), data=payload)

    @staticmethod
    @allure.step('Авторизация пользовтеля')
    def login(payload=None, headers=None):
        if not payload:
            raise Exception('Данные пользователя для авторизации не переданы')
        return requests.post(endpoints.get('login'), data=payload, headers=headers)

    @staticmethod
    @allure.step('Изменение данных пользовтеля')
    def update(payload=None, headers=None):
        if not payload:
            raise Exception('Данные пользователя для изменения не переданы')
        return requests.patch(endpoints.get('user'), data=payload, headers=headers)

    @staticmethod
    @allure.step('Удаление пользовтеля')
    def delete(headers=None):
        if not headers:
            raise Exception('Данные пользователя для удаления не переданы')
        return requests.delete(endpoints.get('user'), data=None, headers=headers)