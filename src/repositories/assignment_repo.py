"""Репозиторий для работы с таблицей assignments."""

from src.database import get_connection
from src.models.assignment import Assignment


def _map(row) -> Assignment:
    return Assignment(*row)


def create(employee_id: int, position_id: int, start_date: str,
           end_date: str | None = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO assignments(employee_id, position_id, start_date, end_date)
        VALUES (?, ?, ?, ?)
    """, (employee_id, position_id, start_date, end_date))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_id(assignment_id: int) -> Assignment | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM assignments WHERE assignment_id = ?", (assignment_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all_with_details() -> list[Assignment]:
    """Возвращает назначения с ФИО сотрудника и названием должности (JOIN)."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.assignment_id, a.employee_id, a.position_id,
               a.start_date, a.end_date,
               e.last_name || ' ' || e.first_name AS emp_name,
               p.title
        FROM assignments a
        JOIN employees e ON a.employee_id = e.employee_id
        JOIN positions p ON a.position_id = p.position_id
        ORDER BY a.assignment_id
    """)
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def close_assignment(assignment_id: int, end_date: str) -> None:
    """Закрывает назначение — ставит дату окончания."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE assignments SET end_date = ? WHERE assignment_id = ?",
                (end_date, assignment_id))
    conn.commit()
    conn.close()


def delete(assignment_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM assignments WHERE assignment_id = ?", (assignment_id,))
    conn.commit()
    conn.close()
