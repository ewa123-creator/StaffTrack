"""Модель назначения на должность."""

from dataclasses import dataclass


@dataclass
class Assignment:
    assignment_id: int
    employee_id: int
    position_id: int
    start_date: str
    end_date: str | None = None

    # Служебные поля (не хранятся в БД, заполняются при JOIN-запросах)
    employee_full_name: str | None = None
    position_title: str | None = None
