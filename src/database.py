"""Модуль для работы с базой данных SQLite (StaffTrack)."""

import os
import sqlite3

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DB_PATH     = os.path.join(PROJECT_DIR, "stafftrack.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")


def get_connection():
    """Возвращает соединение с БД с включёнными внешними ключами."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    """Создаёт таблицы и заполняет их начальными данными."""
    conn = get_connection()
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        print("База данных успешно инициализирована.")
    finally:
        conn.close()


def get_employees_with_positions():
    """Возвращает сотрудников с их должностями (JOIN)."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT e.employee_id, e.last_name, e.first_name, p.title, a.start_date
            FROM   assignments a
            JOIN   employees e ON a.employee_id = e.employee_id
            JOIN   positions p ON a.position_id = p.position_id
            ORDER  BY e.employee_id;
        """)
        return cur.fetchall()
    finally:
        conn.close()


def get_positions():
    """Возвращает список должностей."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT position_id, title, salary FROM positions ORDER BY position_id;")
        return cur.fetchall()
    finally:
        conn.close()
