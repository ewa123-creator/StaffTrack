"""Модель руководителя подразделения."""

from dataclasses import dataclass


@dataclass
class Manager:
    manager_id: int
    employee_id: int
    appointed_date: str | None = None
