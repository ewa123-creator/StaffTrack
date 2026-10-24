"""Репозиторий для работы с таблицей managers."""

from src.database import get_connection
from src.models.manager import Manager


def _map(row) -> Manager:
    return Manager(*row)


def create(employee_id: int, appointed_date: str | None = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO managers(employee_id, appointed_date)
        VALUES (?, ?)
    """, (employee_id, appointed_date))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_employee(employee_id: int) -> Manager | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM managers WHERE employee_id = ?", (employee_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all() -> list[Manager]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM managers ORDER BY manager_id")
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def delete(manager_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM managers WHERE manager_id = ?", (manager_id,))
    conn.commit()
    conn.close()
