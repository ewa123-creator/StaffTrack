"""Репозиторий для работы с таблицей assignments."""

from src.stafftrack.database.database import get_connection
from src.stafftrack.models.assignment import Assignment
from src.stafftrack.repositories import queries


def _map(row) -> Assignment:
    return Assignment(*row)


def create(employee_id: int, position_id: int, start_date: str,
           end_date: str | None = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.INSERT_ASSIGNMENT, (employee_id, position_id, start_date, end_date))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_by_id(assignment_id: int) -> Assignment | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.SELECT_ASSIGNMENT_BY_ID, (assignment_id,))
    row = cur.fetchone()
    conn.close()
    return _map(row) if row else None


def get_all_with_details() -> list[Assignment]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.SELECT_ALL_ASSIGNMENTS_WITH_DETAILS)
    rows = cur.fetchall()
    conn.close()
    return [_map(r) for r in rows]


def close_assignment(assignment_id: int, end_date: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.CLOSE_ASSIGNMENT, (end_date, assignment_id))
    conn.commit()
    conn.close()


def delete(assignment_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(queries.DELETE_ASSIGNMENT, (assignment_id,))
    conn.commit()
    conn.close()
