from generators import generate_courier

class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    DELETE_COURIER = '/api/v1/courier/'

class Users():

    courier_data = generate_courier()

    false_login_data = {
        "login": 'false_' + courier_data["login"],
        "password": courier_data["password"]
    }

    false_password_data = {
        "login": courier_data["login"],
        "password": 'false_' + courier_data["password"]
    }

    not_login_data = {
        "login": '',
        "password": courier_data["password"]
    }

    not_password_data = {
        "login": courier_data["login"],
        "password": ''
    }