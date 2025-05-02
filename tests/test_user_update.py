import pytest
import allure

@allure.suite('Изменение данных пользователя')
@pytest.mark.usefixtures('register_class')
class TestUserUpdate:
    @allure.title('C авторизацией')
    def test_user_update_authorized(self, user):
        self.credentials['email'] = user.generate()['email']
        response = user.update(self.credentials, self.headers)
        assert (response.status_code == 200
                and response.json().get('success'))

    @allure.title('Без авторизации')
    def test_user_update_unauthorized(self, user):
        for type in ['email', 'password']:
            self.credentials[type] = user.generate()[type]
            response = user.update(self.credentials)
            data = response.json()
            assert (response.status_code == 401
                    and data.get('success') is False
                    and data.get('message') == 'You should be authorised')