class TestLoginUser:
    def test_login_user_success(self, user_methods):
        response = user_methods.login_user_success()
        assert response.status_code == 200 and response.json()["success"] == True

    def test_wrong_email_and_password(self, user_methods):
        response = user_methods.wrong_email_and_password()
        assert response.status_code == 401 and response.json()["message"] == ("email or password are incorrect")
