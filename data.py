from generators import generate_courier

class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    GET_LIST_ORDERS = '/api/v1/orders'
    CANCEL_ORDER = '/api/v1/orders/cancel'
    DELETE_COURIER = '/api/v1/courier/'


class Users:

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

class Orders:
    data_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }