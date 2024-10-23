import pytest
import requests
from helpers import CreateUser
from data import Urls


class TestCreateOrder:
    def test_create_order_success(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        response_ingridients = requests.get(Urls.URL + Urls.INGREDIENTS)
        payload_ingridients = {"ingredients": [response_ingridients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})

        assert response_order.status_code == 200 and "true" in response_order.text

    def test_create_order_no_autorization(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        response_ingridients = requests.get(Urls.URL + Urls.INGREDIENTS)
        payload_ingridients = {"ingredients": [response_ingridients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients)

        assert response_order.status_code == 200 and 'true' in response_order.text

    def test_create_order_no_ingredients(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        payload_ingridients = {"ingredients": []}
        response_order = requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})

        assert response_order.status_code == 400 and 'true' in response.text

    def test_create_order_invalid_hesh(self):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        payload_ingridients = {"ingredients": ["61c0c5a71d1f820"]}
        response_order = requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})

        assert response_order.status_code == 500 and "Internal Server Error" in response_order.text
