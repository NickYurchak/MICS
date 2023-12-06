from user import User

# Клас для будівництва користувача
class UserBuilder:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.age = None
        self.city = None

    def set_age(self, age):
        self.age = age
        return self

    def set_city(self, city):
        self.city = city
        return self

    def build(self):
        return User(self.username, self.email, self.password, self.age, self.city)