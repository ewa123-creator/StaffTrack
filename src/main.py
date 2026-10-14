"""StaffTrack — точка входа."""

import os
from database import DB_PATH, init_db, get_employees_with_positions, get_positions


def print_positions():
    print("\nДолжности:")
    print("-" * 45)
    for pos_id, title, salary in get_positions():
        print(f"  {pos_id}. {title} — {salary} руб.")
    print("-" * 45)


def print_employees():
    print("\nСотрудники с должностями:")
    print("-" * 70)
    for emp_id, last, first, position, start in get_employees_with_positions():
        print(f"  {emp_id}. {last} {first} — {position} (с {start})")
    print("-" * 70)


def main():
    if not os.path.exists(DB_PATH):
        init_db()

    print("=== StaffTrack: система учёта сотрудников ===")
    print_positions()
    print_employees()


if __name__ == "__main__":
    main()
