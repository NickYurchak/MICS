# Клас користувача
class User:
    def __init__(self, username, email, password, age=None, city=None):
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.city = city

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Age: {self.age}, City: {self.city}"