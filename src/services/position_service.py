"""Бизнес-логика для должностей."""

from src.repositories import position_repo, assignment_repo
from src.models.position import Position


def create_position(title: str, salary: float, staff_units: int) -> int:
    if not title.strip():
        raise Exception("Название должности обязательно")
    if salary <= 0:
        raise Exception("Оклад должен быть больше нуля")
    if staff_units <= 0:
        raise Exception("Количество ставок должно быть больше нуля")
    return position_repo.create(title, salary, staff_units)


def get_all() -> list[Position]:
    return position_repo.get_all()


def get_occupied_count(position_id: int) -> int:
    """Считает занятые ставки по действующим назначениям."""
    assignments = assignment_repo.get_all_with_details()
    count = 0
    for a in assignments:
        if a.position_id == position_id and a.end_date is None:
            count += 1
    return count


def get_free_count(position_id: int) -> int:
    """Сколько свободных ставок осталось."""
    pos = position_repo.get_by_id(position_id)
    if not pos:
        return 0
    return pos.staff_units - get_occupied_count(position_id)
