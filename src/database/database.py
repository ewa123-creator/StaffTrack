"""Модуль для работы с базой данных SQLite (StaffTrack)."""

import os
import sqlite3
import hashlib

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
SRC_DIR     = os.path.dirname(BASE_DIR)
PROJECT_DIR = os.path.dirname(SRC_DIR)

DB_PATH = os.path.join(PROJECT_DIR, "stafftrack.db")


def get_connection():
    """Возвращает соединение с БД с включёнными внешними ключами."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def hash_password(password: str) -> str:
    """Превращает пароль в хэш (SHA-256)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def init_db():
    """Создаёт таблицы и заполняет их начальными данными."""
    conn = get_connection()
    cur = conn.cursor()
    
    # Удаляем старые таблицы, если есть
    cur.executescript("""
        DROP TABLE IF EXISTS assignments;
        DROP TABLE IF EXISTS managers;
        DROP TABLE IF EXISTS positions;
        DROP TABLE IF EXISTS employees;
    """)

    # Создаем таблицы
    cur.executescript("""
        CREATE TABLE employees (
            employee_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            personnel_number TEXT    NOT NULL UNIQUE,
            last_name        TEXT    NOT NULL,
            first_name       TEXT    NOT NULL,
            middle_name      TEXT,
            birth_date       DATE,
            phone            TEXT,
            login            TEXT    NOT NULL UNIQUE,
            password_hash    TEXT    NOT NULL,
            dismissal_date   DATE
        );

        CREATE TABLE positions (
            position_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            title        TEXT    NOT NULL,
            salary       REAL    NOT NULL,
            staff_units  INTEGER NOT NULL
        );

        CREATE TABLE assignments (
            assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id   INTEGER NOT NULL,
            position_id   INTEGER NOT NULL,
            start_date    DATE    NOT NULL,
            end_date      DATE,
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
            FOREIGN KEY (position_id) REFERENCES positions (position_id)
        );

        CREATE TABLE managers (
            manager_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id    INTEGER NOT NULL UNIQUE,
            appointed_date DATE,
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        );
    """)

    # Хэшируем пароли
    hr_hash = hash_password("hr123")
    mgr_hash = hash_password("mgr123")
    petrova_hash = hash_password("123")

    # Вставляем тестовые данные
    cur.executescript(f"""
        INSERT INTO employees (personnel_number, last_name, first_name, middle_name, birth_date, phone, login, password_hash) VALUES
        ('001', 'Сорокина', 'Ева',   'Андреевна',  '1990-05-12', '+7-900-111-22-33', 'hr',      '{hr_hash}'),
        ('002', 'Иванов',   'Иван',  'Петрович',   '1985-03-20', '+7-900-222-33-44', 'manager', '{mgr_hash}'),
        ('003', 'Петрова',  'Анна',  'Сергеевна',  '1992-11-08', '+7-900-333-44-55', 'petrova', '{petrova_hash}');

        INSERT INTO positions (title, salary, staff_units) VALUES
        ('Кадровик',   70000.0, 1),
        ('Менеджер',   90000.0, 2),
        ('Бухгалтер',  80000.0, 1);

        INSERT INTO assignments (employee_id, position_id, start_date) VALUES
        (1, 1, '2026-09-28'),
        (2, 2, '2025-01-15'),
        (3, 3, '2026-03-01');

        INSERT INTO managers (employee_id, appointed_date) VALUES
        (2, '2025-01-15');
    """)
    
    conn.commit()
    conn.close()
    print("База данных успешно инициализирована.")
