import pytest
from helpers import CreateUser


class TestUser:
    def test_create_user(self, user_methods):
        response_user = user_methods.create_user()
        assert response_user.status_code == 200

    def test_create_same_data_registration(self, user_methods):
        response_user = user_methods.create_user_same_data_registration()
        assert response_user.status_code == 403 and response_user.json()["message"] == 'User already exists'

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
    def test_create_courier_no_one_param_registration(self, email, password, name, user_methods):
        response = user_methods.create_courier_no_one_param_registration(email, password, name)
        assert response.status_code == 403 and response.json()["message"] == ('Email, password and name are required '
                                                                              'fields')
