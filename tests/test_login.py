import pytest
import allure

@allure.suite('Логин пользовтаеля')
@pytest.mark.usefixtures('register_class')
class TestLogin:
    @allure.title('Логин под существующим пользователем')
    def test_login_success(self, user):
        response = user.login(self.credentials)
        assert (response.status_code == 200
                and response.json().get('success'))

    @allure.title('Логин с неверным логином и паролем')
    def test_login_error(self, user):
        del self.credentials['email']
        response = user.login(self.credentials)
        data = response.json()
        assert (response.status_code == 401
                and data.get('message') == 'email or password are incorrect')