import pytest
import requests

from helpers import CreateUser
from data import Urls, user_data
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@pytest.fixture
def order_methods():
    return OrderMethods()


@pytest.fixture
def user_methods():
    return UserMethods()


@pytest.fixture()
def create_new_user():
    login_password, response = CreateUser.register_new_user_and_return_login_password()
    yield login_password
    requests.delete(Urls.URL + Urls.ACTION_USER, headers={'authorization': response.json()["accessToken"]})


@pytest.fixture
def authorization():
    if user_data.get('login'):
        payload = {"email": user_data.get('login'), "password": user_data.get('password')}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
    else:
        login_password, response = CreateUser.register_new_user_and_return_login_password()
    return response.json()["accessToken"]

