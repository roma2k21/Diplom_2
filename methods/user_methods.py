import json
from typing import Optional
import requests
from data import Urls
from helpers import CreateUser


class UserMethods:
    base_url = Urls.URL

    def __init__(self):
        self.payload = None
        self.email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        self.password = CreateUser.generate_random_string(10)
        self.name = CreateUser.generate_random_string(5)

    def create_user(self):
        self.payload = {"email": self.email, "password": self.password, "name": self.name}
        response = requests.post(url=f'{self.base_url}{Urls.CREATE_USER}', data=self.payload)
        return response

    def create_user_same_data_registration(self):
        self.create_user()
        response = requests.post(url=f'{self.base_url}{Urls.CREATE_USER}', data=self.payload)
        return response

    def create_courier_no_one_param_registration(self, email, password, name):
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(Urls.URL + Urls.CREATE_USER, data=payload)
        return response

    def change_data_user_success(self):
        response = self.create_user()
        token = response.json()["accessToken"]
        new_email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        new_payload = {"email": new_email}
        change_response = requests.patch(Urls.URL + Urls.ACTION_USER, data=new_payload,
                                         headers={"Authorization": token})
        return change_response

    def change_data_user_error(self):
        self.create_user()
        new_email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        new_payload = {"email": new_email}
        change_response = requests.patch(Urls.URL + Urls.ACTION_USER, data=new_payload)
        return change_response

    def login_user_success(self):
        self.create_user()
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=self.payload)
        return response

    def wrong_email_and_password(self):
        self.create_user()
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        payload = {"email": email, "password": password}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        return response
