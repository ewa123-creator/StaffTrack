"""Консольные меню StaffTrack."""

from src.services import employee_service, position_service, assignment_service, auth_service


def hr_menu(user):
    while True:
        print(f"\n===== Кадровик: {user.first_name} {user.last_name} =====")
        print("1. Список сотрудников")
        print("2. Список должностей")
        print("3. Все назначения")
        print("4. Назначить сотрудника на должность")
        print("5. Уволить сотрудника")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            _print_employees()
        elif choice == "2":
            _print_positions()
        elif choice == "3":
            _print_assignments()
        elif choice == "4":
            _create_assignment()
        elif choice == "5":
            _dismiss_employee()
        elif choice == "0":
            break


def manager_menu(user):
    while True:
        print(f"\n===== Руководитель: {user.first_name} {user.last_name} =====")
        print("1. Список сотрудников")
        print("2. Список должностей")
        print("3. Все назначения")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            _print_employees()
        elif choice == "2":
            _print_positions()
        elif choice == "3":
            _print_assignments()
        elif choice == "0":
            break


def _print_employees():
    print("\nСотрудники:")
    for e in employee_service.get_all():
        status = "уволен" if e.dismissal_date else "работает"
        print(f"  [{e.employee_id}] {e.last_name} {e.first_name} — {status}")


def _print_positions():
    print("\nДолжности:")
    for p in position_service.get_all():
        free = position_service.get_free_count(p.position_id)
        print(f"  [{p.position_id}] {p.title} — оклад {p.salary} — свободно {free} из {p.staff_units}")


def _print_assignments():
    print("\nНазначения:")
    for a in assignment_service.get_all():
        end = a.end_date or "по наст. время"
        print(f"  [{a.assignment_id}] {a.employee_full_name} — {a.position_title} ({a.start_date} — {end})")


def _create_assignment():
    try:
        emp_id = int(input("ID сотрудника: "))
        pos_id = int(input("ID должности: "))
        start = input("Дата начала (YYYY-MM-DD): ")
        assignment_service.create_assignment(emp_id, pos_id, start)
        print("✅ Назначение оформлено")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def _dismiss_employee():
    try:
        emp_id = int(input("ID сотрудника: "))
        date = input("Дата увольнения (YYYY-MM-DD): ")
        assignment_service.dismiss_employee(emp_id, date)
        print("✅ Сотрудник уволен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
