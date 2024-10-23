import pytest
import requests
from helpers import CreateUser
from data import Urls


class TestLoginUser:
    def test_create_same_data_registration(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        assert response.status_code == 200 and 'true' in response.text

    def test_wrong_email_and_password(self):
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        payload = {"email": email, "password": password}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        assert response.status_code == 401 and response.json()["message"] == ("email or password are incorrect")
