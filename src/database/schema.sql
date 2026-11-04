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

-- Пароли захэшированы (hr123, mgr123, 123)
INSERT INTO employees (personnel_number, last_name, first_name, middle_name, birth_date, phone, login, password_hash) VALUES
('001', 'Сорокина', 'Ева',   'Андреевна',  '1990-05-12', '+7-900-111-22-33', 'hr',      '1229e4a8f8458fb98b297d2d12e12eb2c5e1a8a64b55a2643e38fb742f14c8f2'),
('002', 'Иванов',   'Иван',  'Петрович',   '1985-03-20', '+7-900-222-33-44', 'manager', 'e9b0221e2ec89c607c4bc1d8b23491b2051db71cc3612c39df807b6c3e8c4427'),
('003', 'Петрова',  'Анна',  'Сергеевна',  '1992-11-08', '+7-900-333-44-55', 'petrova', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

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
