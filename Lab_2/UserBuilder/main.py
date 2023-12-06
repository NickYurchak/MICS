from user_builder import UserBuilder

# Використання паттерну "Будівельник" для реєстрації користувача
user1 = UserBuilder("McVilka", "mcvilka@example.com", "password123").build()
print(user1)

user2 = UserBuilder("NickY", "nicky@example.com", "qwerty123").set_age(30).set_city("New York").build()
print(user2)
