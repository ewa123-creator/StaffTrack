"""Сервис авторизации."""

from src.repositories import employee_repo, manager_repo
from src.models.employee import Employee


def authenticate(login: str, password: str) -> Employee | None:
    """Проверяет логин/пароль. Возвращает сотрудника или None."""
    user = employee_repo.get_by_login(login)
    if not user:
        return None
    # В учебном проекте пароль хранится открыто (в реальном — хэш)
    if user.password_hash != password:
        return None
    return user


def get_role(user: Employee) -> str:
    """Определяет роль: 'manager' если есть в managers, иначе 'hr'."""
    mgr = manager_repo.get_by_employee(user.employee_id)
    return "manager" if mgr else "hr"
