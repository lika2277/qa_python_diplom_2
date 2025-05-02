import pytest
import allure

@allure.suite('Создание нового пользовтаеля')
class TestRegister:
    @allure.title('Создать уникального пользователя')
    def test_register_uniq(self, user, register_function):
        response, _ = register_function(user.generate())
        assert (response.status_code == 200
                and response.json().get('success'))

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_register_exists(self, user, register_function):
        credentials = user.generate()
        register_function(credentials)
        response = user.register(credentials)
        data = response.json()
        assert (response.status_code == 403
                and data.get('success') is False
                and data.get('message') == 'User already exists')

    @allure.title('Создать пользователя и не заполнить одно из обязательных полей')
    def test_register_skip(self, user, register_function):
        credentials = user.generate()
        del credentials['email']
        response, _ = register_function(credentials)
        data = response.json()
        assert (response.status_code == 403
                and data.get('success') is False
                and data.get('message') == 'Email, password and name are required fields')