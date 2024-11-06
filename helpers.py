import requests
import random
import string
from data import Urls


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список


class CreateUser:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_new_user_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра,
        # в качестве параметра передаём длину строки
        # создаём список, чтобы метод мог его вернуть
        login_pass = []  # генерируем логин, пароль
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        name = CreateUser.generate_random_string(5)
        payload = {"email": email, "password": password, "name": name}
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.URL + Urls.CREATE_USER,
                                 data=payload)  # если регистрация прошла успешно (код ответа 200),
        # добавляем в список логин и пароль
        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)
        # возвращаем список
        return login_pass, response
