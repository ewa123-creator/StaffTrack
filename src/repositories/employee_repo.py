"""Репозиторий для работы с таблицей employees."""

from src.database import get_connection
from src.models.employee import Employee


def _map(row) -> Employee:
    return Employee(*row)


def create(personnel_number: str, last_name: str, first_name: str,
           middle_name: str | None = None, birth_date: str | None = None,
           phone: str | None = None, login: str = "", password_hash: str = "") -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO employees(personnel_number, last_name, first_name,
                              middle_name, birth_date, phone, login, password_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (personnel_number, last_name, first_name, middle_name,
          birth_date, phone, login, password_hash))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_id(employee_id: int) -> Employee | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_by_login(login: str) -> Employee | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE login = ?", (login,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all() -> list[Employee]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees ORDER BY employee_id")
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def update(employee_id: int, **fields) -> None:
    if not fields:
        return
    set_clause = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [employee_id]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE employees SET {set_clause} WHERE employee_id = ?", values)
    conn.commit()
    conn.close()


def delete(employee_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
    conn.commit()
    conn.close()
