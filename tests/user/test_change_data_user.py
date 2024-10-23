import pytest
import requests
from helpers import CreateUser
from data import Urls


class TestChangeDataUser:
    def test_change_data_user_success(self):
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        name = CreateUser.generate_random_string(5)
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(Urls.URL + Urls.CREATE_USER, data=payload)
        new_email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        new_payload = {"email": new_email}
        change_response = requests.patch(Urls.URL + Urls.ACTION_USER, data=new_payload, headers={'authorization': response.json()["accessToken"]})
        assert change_response.status_code == 200 and 'true' in response.text

    def test_change_data_user_error(self):
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        name = CreateUser.generate_random_string(5)
        payload = {"email": email, "password": password, "name": name}
        new_email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        new_payload = {"email": new_email}
        change_response = requests.patch(Urls.URL + Urls.ACTION_USER, data=new_payload)

        assert change_response.status_code == 401 and change_response.json()["message"] == "You should be authorised"
