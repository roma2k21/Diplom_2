class TestChangeDataUser:
    def test_change_data_user_success(self, authorization, user_methods):
        change_response = user_methods.change_data_user_success()
        assert change_response.status_code == 200 and change_response.json()["success"] == True

    def test_change_data_user_error(self, user_methods):
        change_response = user_methods.change_data_user_error()
        assert change_response.status_code == 401 and change_response.json()["success"] == False
