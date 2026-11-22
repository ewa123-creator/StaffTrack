import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml

from src.stafftrack.database.database import get_connection

def export_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.employee_id, e.last_name, e.first_name, e.phone, p.title
        FROM employees e
        LEFT JOIN assignments a ON e.employee_id = a.employee_id AND a.end_date IS NULL
        LEFT JOIN positions p ON a.position_id = p.position_id
    """)
    rows = cur.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "last_name": row[1],
            "first_name": row[2],
            "phone": row[3],
            "position": row[4] if row[4] else "Не назначен"
        })

    os.makedirs("out", exist_ok=True)

    with open("out/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open("out/data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "last_name", "first_name", "phone", "position"])
        writer.writeheader()
        writer.writerows(data)

    root = ET.Element("employees")
    for item in data:
        emp = ET.SubElement(root, "employee")
        for key, value in item.items():
            child = ET.SubElement(emp, key)
            child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write("out/data.xml", encoding="utf-8", xml_declaration=True)

    with open("out/data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

    print("Данные выгружены в папку out/")
