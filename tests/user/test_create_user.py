import pytest
import requests
from helpers import CreateUser
from data import Urls


class TestUser:
    def test_create_user(self):
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        name = CreateUser.generate_random_string(5)
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(Urls.URL + Urls.CREATE_USER, data=payload)
        assert response.status_code == 200

    def test_create_same_data_registration(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1], "name": login_password[2]}
        response = requests.post(Urls.URL + Urls.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.json()["message"] == 'User already exists'

    email = CreateUser.generate_random_string(7) + f"@yandex.ru"
    password = CreateUser.generate_random_string(10)
    name = CreateUser.generate_random_string(5)

    @pytest.mark.parametrize(
        'email, password, name',
        [
            (email, password, ""),
            (email, "", name),
            ("", password, name),
        ]
    )
    def test_create_courier_no_one_param_registration(self, email, password, name):
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(Urls.URL + Urls.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.json()["message"] == ('Email, password and name are required '
                                                                              'fields')
