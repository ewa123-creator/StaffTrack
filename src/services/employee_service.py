"""Бизнес-логика для сотрудников."""

from src.repositories import employee_repo
from src.models.employee import Employee


def create_employee(personnel_number: str, last_name: str, first_name: str,
                    middle_name: str | None, birth_date: str | None,
                    phone: str | None, login: str, password: str) -> int:
    if not personnel_number.strip():
        raise Exception("Табельный номер не может быть пустым")
    if not last_name.strip() or not first_name.strip():
        raise Exception("Фамилия и имя обязательны")
    if not login.strip() or not password.strip():
        raise Exception("Логин и пароль обязательны")

    # Проверка уникальности табельного номера
    for emp in employee_repo.get_all():
        if emp.personnel_number == personnel_number:
            raise Exception("Сотрудник с таким табельным номером уже есть")

    return employee_repo.create(
        personnel_number, last_name, first_name,
        middle_name, birth_date, phone, login, password
    )


def get_all() -> list[Employee]:
    return employee_repo.get_all()


def get_by_id(employee_id: int) -> Employee | None:
    return employee_repo.get_by_id(employee_id)
