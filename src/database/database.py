"""Модуль для работы с базой данных SQLite (StaffTrack)."""

import os
import sqlite3

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
SRC_DIR     = os.path.dirname(BASE_DIR)
PROJECT_DIR = os.path.dirname(SRC_DIR)

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
