"""Бизнес-логика для назначений."""

from datetime import date
from src.repositories import assignment_repo, employee_repo
from src.services import position_service
from src.models.assignment import Assignment


def create_assignment(employee_id: int, position_id: int, start_date: str) -> int:
    # 1. Сотрудник существует и не уволен?
    emp = employee_repo.get_by_id(employee_id)
    if not emp:
        raise Exception("Сотрудник не найден")
    if emp.dismissal_date:
        raise Exception("Сотрудник уже уволен")

    # 2. Есть свободная ставка?
    free = position_service.get_free_count(position_id)
    if free <= 0:
        raise Exception("Свободных ставок по должности нет")

    # 3. Если есть действующее назначение — закрываем его
    for a in get_all():
        if a.employee_id == employee_id and a.end_date is None:
            assignment_repo.close_assignment(a.assignment_id, start_date)

    return assignment_repo.create(employee_id, position_id, start_date)


def dismiss_employee(employee_id: int, dismissal_date: str) -> None:
    emp = employee_repo.get_by_id(employee_id)
    if not emp:
        raise Exception("Сотрудник не найден")
    if emp.dismissal_date:
        raise Exception("Сотрудник уже уволен")

    # Закрываем действующие назначения
    for a in get_all():
        if a.employee_id == employee_id and a.end_date is None:
            assignment_repo.close_assignment(a.assignment_id, dismissal_date)

    # Записываем дату увольнения
    employee_repo.update(employee_id, dismissal_date=dismissal_date)


def get_all() -> list[Assignment]:
    return assignment_repo.get_all_with_details()
