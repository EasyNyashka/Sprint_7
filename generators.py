from faker import Faker

fake = Faker()

def generate_courier():
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    courier_data = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return courier_data

def generate_courier_not_password():
    login = fake.user_name()
    firstName = fake.name()
    courier_data_not_password = {
        "login": login,
        "password": '',
        "name": firstName
    }
    return courier_data_not_password

def generate_courier_not_login():
    password = fake.password()
    firstName = fake.name()
    courier_data_not_login = {
        "login": '',
        "password": password,
        "name": firstName
    }
    return courier_data_not_login



