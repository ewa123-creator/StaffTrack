"""Репозиторий для работы с таблицей managers."""

from src.stafftrack.database.database import get_connection
from src.stafftrack.models.manager import Manager
from src.stafftrack.repositories import queries


def _map(row) -> Manager:
    return Manager(*row)


def create(employee_id: int, appointed_date: str | None = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.INSERT_MANAGER, (employee_id, appointed_date))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_employee(employee_id: int) -> Manager | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.SELECT_MANAGER_BY_EMPLOYEE, (employee_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all() -> list[Manager]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.SELECT_ALL_MANAGERS)
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def delete(manager_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.DELETE_MANAGER, (manager_id,))
    conn.commit()
    conn.close()
