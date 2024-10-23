import pytest
import requests
from helpers import CreateUser
from data import Urls


class TestListOrder:
    def test_get_list_order_autorization_user(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        response_ingridients = requests.get(Urls.URL + Urls.INGREDIENTS)
        payload_ingridients = {"ingredients": [response_ingridients.json()["data"][0]["_id"]]}
        requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})
        response_order_user = requests.get(Urls.URL + Urls.CREATE_ORDER, headers={"Authorization": response.json()["accessToken"]})

        assert response_order_user.status_code == 200 and 'success' in response.text

    def test_get_list_order_no_autorization_user(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        response_ingridients = requests.get(Urls.URL + Urls.INGREDIENTS)
        payload_ingridients = {"ingredients": [response_ingridients.json()["data"][0]["_id"]]}
        requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})
        response_order_user = requests.get(Urls.URL + Urls.CREATE_ORDER)

        assert response_order_user.status_code == 401 and 'true' in response.text
