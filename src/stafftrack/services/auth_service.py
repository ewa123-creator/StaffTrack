"""Сервис авторизации."""

from src.stafftrack.repositories import employee_repo, manager_repo
from src.stafftrack.models.employee import Employee
from src.stafftrack.database.database import hash_password


def authenticate(login: str, password: str) -> Employee | None:
    user = employee_repo.get_by_login(login)
    if not user:
        return None
    
    # Сравниваем хэш введенного пароля с хэшем в базе
    if user.password_hash != hash_password(password):
        return None
        
    return user


def get_role(user: Employee) -> str:
    mgr = manager_repo.get_by_employee(user.employee_id)
    return "manager" if mgr else "hr"
