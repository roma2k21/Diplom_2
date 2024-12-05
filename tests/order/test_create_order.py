import pytest


class TestCreateOrder:
    def test_create_order_success(self, order_methods, authorization):
        response_ingredients = order_methods.get_ingredients()
        response_order = order_methods.create_order(
            payload={
                "ingredients": [response_ingredients["data"][0]["_id"]]
            },
            token=authorization
        )
        assert response_order[0].status_code == 200 and "true" in response_order[0].text

    def test_create_order_no_authorization(self, order_methods):
        response_ingridients = order_methods.get_ingredients()
        response_order = order_methods.create_order(
            payload={
                "ingredients": [response_ingridients["data"][0]["_id"]]
            }
        )

        assert response_order[0].status_code == 200 and 'true' in response_order[0].text

    @pytest.mark.parametrize(
        'payload, expected_status_code, expected_text',
        [
            ({"ingredients": []}, 400, 'false'),
            ({"ingredients": ["61c0c5a71d1f820"]}, 500, 'Internal Server Error')
        ],
        ids=[
            'no_ingredients',
            'invalid_hash',
        ]
    )
    def test_create_order_invalid_ingredients(self, order_methods, authorization, payload, expected_status_code, expected_text):
        response_order = order_methods.create_order(payload=payload, token=authorization)
        assert response_order[0].status_code == expected_status_code and expected_text in response_order[0].text
