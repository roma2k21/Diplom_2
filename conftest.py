import pytest
import requests
from helpers import CreateUser
from data import Urls


@pytest.fixture()
def create_new_user():
    login_password = CreateUser.register_new_user_and_return_login_password()
    data = {"login": login_password[0], "password": login_password[1], "name": login_password[2]}
    response = requests.post(Urls.URL + Urls.CREATE_USER, data)
    yield login_password
    requests.delete(Urls.URL + Urls.ACTION_USER, headers={'authorization': response.json()["accessToken"]})
