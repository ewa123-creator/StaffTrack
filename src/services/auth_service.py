"""Сервис авторизации."""

import hashlib
from src.repositories import employee_repo, manager_repo
from src.models.employee import Employee


def _hash_password(password: str) -> str:
    """Превращает пароль в хэш (SHA-256)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def authenticate(login: str, password: str) -> Employee | None:
    """Проверяет логин/пароль. Возвращает сотрудника или None."""
    user = employee_repo.get_by_login(login)
    if not user:
        return None
    
    # Сравниваем хэш введенного пароля с хэшем из базы
    if user.password_hash != _hash_password(password):
        return None
    return user


def get_role(user: Employee) -> str:
    """Определяет роль: 'manager' если есть в managers, иначе 'hr'."""
    mgr = manager_repo.get_by_employee(user.employee_id)
    return "manager" if mgr else "hr"
