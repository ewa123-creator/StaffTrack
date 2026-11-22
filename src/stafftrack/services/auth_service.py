"""Сервис авторизации."""

from src.stafftrack.repositories import employee_repo, manager_repo
from src.stafftrack.models.employee import Employee


def authenticate(login: str, password: str) -> Employee | None:
    user = employee_repo.get_by_login(login)
    if not user:
        return None
    if user.password_hash != password:
        return None
    return user


def get_role(user: Employee) -> str:
    mgr = manager_repo.get_by_employee(user.employee_id)
    return "manager" if mgr else "hr"
