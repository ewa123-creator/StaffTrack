"""Авторизация."""

from src.services import auth_service


def login():
    print("\n===== Вход =====")
    login_val = input("Логин: ")
    password = input("Пароль: ")
    user = auth_service.authenticate(login_val, password)
    if not user:
        print("❌ Неверный логин или пароль")
        return None
    print(f"✅ Добро пожаловать, {user.first_name}!")
    return user
