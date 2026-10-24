"""StaffTrack — точка входа."""

import os
import sys

# Добавляем корень проекта в путь (чтобы работали импорты src.*)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, PROJECT_DIR)

from src.database import DB_PATH, init_db
from src.ui import auth, menus
from src.services import auth_service


def main():
    if not os.path.exists(DB_PATH):
        init_db()

    while True:
        print("\n===== StaffTrack =====")
        print("1. Войти")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            user = auth.login()
            if user:
                role = auth_service.get_role(user)
                if role == "manager":
                    menus.manager_menu(user)
                else:
                    menus.hr_menu(user)
        elif choice == "0":
            print("До свидания!")
            break


if __name__ == "__main__":
    main()
