-- ============================================
-- StaffTrack — схема базы данных
-- ============================================

DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS managers;
DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    personnel_number TEXT    NOT NULL UNIQUE,
    last_name        TEXT    NOT NULL,
    first_name       TEXT    NOT NULL,
    middle_name      TEXT,
    birth_date       TEXT,
    phone            TEXT,
    password_hash    TEXT    NOT NULL,
    dismissal_date   TEXT
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
    start_date    TEXT    NOT NULL,
    end_date      TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
    FOREIGN KEY (position_id) REFERENCES positions (position_id)
);

CREATE TABLE managers (
    manager_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id    INTEGER NOT NULL UNIQUE,
    appointed_date TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);

-- Тестовые данные
INSERT INTO employees (personnel_number, last_name, first_name, middle_name, birth_date, phone, password_hash) VALUES
('001', 'Сорокина', 'Ева',   'Андреевна',  '1990-05-12', '+7-900-111-22-33', 'hash_001'),
('002', 'Иванов',   'Иван',  'Петрович',   '1985-03-20', '+7-900-222-33-44', 'hash_002'),
('003', 'Петрова',  'Анна',  'Сергеевна',  '1992-11-08', '+7-900-333-44-55', 'hash_003');

INSERT INTO positions (title, salary, staff_units) VALUES
('Кадровик',   70000.0, 1),
('Менеджер',   90000.0, 2),
('Бухгалтер',  80000.0, 1);

INSERT INTO assignments (employee_id, position_id, start_date) VALUES
(1, 1, '2026-09-28'),
(2, 2, '2025-01-15'),
(3, 3, '2026-03-01');

INSERT INTO managers (employee_id, appointed_date) VALUES
(1, '2026-09-28');
