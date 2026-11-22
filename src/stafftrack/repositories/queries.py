"""Все SQL-запросы для работы с БД."""

# --- Сотрудники (employees) ---
INSERT_EMPLOYEE = """
    INSERT INTO employees(personnel_number, last_name, first_name,
                          middle_name, birth_date, phone, login, password_hash)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""
SELECT_EMPLOYEE_BY_ID = "SELECT * FROM employees WHERE employee_id = ?"
SELECT_EMPLOYEE_BY_LOGIN = "SELECT * FROM employees WHERE login = ?"
SELECT_ALL_EMPLOYEES = "SELECT * FROM employees ORDER BY employee_id"
DELETE_EMPLOYEE = "DELETE FROM employees WHERE employee_id = ?"
# Для update запрос формируется динамически (зависит от полей), его оставим в репозитории.

# --- Должности (positions) ---
INSERT_POSITION = """
    INSERT INTO positions(title, salary, staff_units)
    VALUES (?, ?, ?)
"""
SELECT_POSITION_BY_ID = "SELECT * FROM positions WHERE position_id = ?"
SELECT_ALL_POSITIONS = "SELECT * FROM positions ORDER BY position_id"
DELETE_POSITION = "DELETE FROM positions WHERE position_id = ?"

# --- Назначения (assignments) ---
INSERT_ASSIGNMENT = """
    INSERT INTO assignments(employee_id, position_id, start_date, end_date)
    VALUES (?, ?, ?, ?)
"""
SELECT_ASSIGNMENT_BY_ID = "SELECT * FROM assignments WHERE assignment_id = ?"
SELECT_ALL_ASSIGNMENTS_WITH_DETAILS = """
    SELECT a.assignment_id, a.employee_id, a.position_id,
           a.start_date, a.end_date,
           e.last_name || ' ' || e.first_name AS emp_name,
           p.title
    FROM assignments a
    JOIN employees e ON a.employee_id = e.employee_id
    JOIN positions p ON a.position_id = p.position_id
    ORDER BY a.assignment_id
"""
CLOSE_ASSIGNMENT = "UPDATE assignments SET end_date = ? WHERE assignment_id = ?"
DELETE_ASSIGNMENT = "DELETE FROM assignments WHERE assignment_id = ?"

# --- Руководители (managers) ---
INSERT_MANAGER = "INSERT INTO managers(employee_id, appointed_date) VALUES (?, ?)"
SELECT_MANAGER_BY_EMPLOYEE = "SELECT * FROM managers WHERE employee_id = ?"
SELECT_ALL_MANAGERS = "SELECT * FROM managers ORDER BY manager_id"
DELETE_MANAGER = "DELETE FROM managers WHERE manager_id = ?"
