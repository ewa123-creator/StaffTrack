"""Модель сотрудника."""

from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: int
    personnel_number: str
    last_name: str
    first_name: str
    middle_name: str | None = None
    birth_date: str | None = None
    phone: str | None = None
    login: str = ""
    password_hash: str = ""
    dismissal_date: str | None = None
