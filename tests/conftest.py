import pytest
from instances.user import User
from instances.ingredients import Ingredients
from instances.order import Order

@pytest.fixture(scope='function')
def user():
    return User

@pytest.fixture(scope='function')
def order():
    return Order

@pytest.fixture(scope='function')
def ingredients():
    return Ingredients().get_random_hashes()

@pytest.fixture(scope='function')
def register_function():
    headers = {'Authorization': None}
    def _register(credentials):
        response = User.register(credentials)
        data = response.json()
        if data and 'accessToken' in data:
            headers['Authorization'] = data['accessToken']
        return response, credentials
    yield _register
    if headers['Authorization'] is not None:
        User.delete(headers)

@pytest.fixture(scope='class')
def register_class(request):
    credentials = User.generate()
    request.cls.headers = {'Authorization': None}
    request.cls.credentials = credentials
    response = User.register(credentials)
    data = response.json()
    if data and 'accessToken' in data:
        request.cls.headers['Authorization'] = data['accessToken']
    yield
    if request.cls.headers['Authorization'] is not None:
        User.delete(request.cls.headers)