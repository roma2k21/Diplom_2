class TestListOrder:
    def test_get_list_order_authorization_user(self, order_methods, authorization):
        response_ingridients = order_methods.get_ingredients()
        order_methods.create_order(
            payload={
                "ingredients": [response_ingridients["data"][0]["_id"]]
            },
            token=authorization
        )
        response_order_list = order_methods.get_list_order(token=authorization)

        assert response_order_list.status_code == 200 and response_order_list.json()["success"] == True

    def test_get_list_order_no_authorization_user(self, order_methods):
        response_ingridients = order_methods.get_ingredients()
        order_methods.create_order(
            payload={
                "ingredients": [response_ingridients["data"][0]["_id"]]
            }
        )
        response_order_list = order_methods.get_list_order()

        assert response_order_list.status_code == 401 and response_order_list.json()["success"] == False
