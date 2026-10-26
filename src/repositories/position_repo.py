"""Репозиторий для работы с таблицей positions."""

from src.database.database import get_connection
from src.models.position import Position


def _map(row) -> Position:
    return Position(*row)


def create(title: str, salary: float, staff_units: int) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO positions(title, salary, staff_units)
        VALUES (?, ?, ?)
    """, (title, salary, staff_units))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_id(position_id: int) -> Position | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM positions WHERE position_id = ?", (position_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all() -> list[Position]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM positions ORDER BY position_id")
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def update(position_id: int, **fields) -> None:
    if not fields:
        return
    set_clause = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [position_id]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE positions SET {set_clause} WHERE position_id = ?", values)
    conn.commit()
    conn.close()


def delete(position_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM positions WHERE position_id = ?", (position_id,))
    conn.commit()
    conn.close()
