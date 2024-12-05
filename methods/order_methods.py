import json
from typing import Optional

import requests
from requests import Response

from data import Urls


class OrderMethods:
    base_url = Urls.URL

    def get_ingredients(self):
        """
        Получить список ингредиентов.

        :return:  Словарь с ID ингредиентов
        """
        response_ingredients = requests.get(f'{self.base_url}{Urls.INGREDIENTS}')
        return response_ingredients.json()

    def create_order(self, payload: dict, token: Optional[str] = None) -> tuple[Response, Optional[dict]]:
        """
        Создает заказ

        :param payload: Данные для создания заказа
        :param token:   Токен пользователя
        :return:        Данные заказа
        """
        response_order = requests.post(f'{self.base_url}{Urls.CREATE_ORDER}', data=payload,
                                       headers={"Authorization": token})
        try:
            json_response = response_order.json()
        except json.JSONDecodeError:
            json_response = None
        return response_order, json_response

    def get_list_order(self, token: Optional[str] = None):
        response_order_user = requests.get(f'{self.base_url}{Urls.CREATE_ORDER}',
                                           headers={"Authorization": token})
        return response_order_user
