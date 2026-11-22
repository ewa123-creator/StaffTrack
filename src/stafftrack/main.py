"""StaffTrack — точка входа."""

import os
from src.stafftrack.database.database import DB_PATH, init_db
from src.stafftrack.ui import auth, menus
from src.stafftrack.services import auth_service


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
