import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml
from src.stafftrack.database.database import get_connection

def export_table(table_name: str):
    """Универсальная выгрузка данных из указанной таблицы."""
    conn = get_connection()
    cur = conn.cursor()
    
    # Получаем названия колонок для выбранной таблицы
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cur.fetchall()]
    
    # Делаем запрос к таблице
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    conn.close()

    # Преобразуем в список словарей
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))

    # Создаём папку out (в корне проекта)
    os.makedirs("out", exist_ok=True)

    # 1. JSON
    with open(f"out/{table_name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # 2. CSV
    with open(f"out/{table_name}.csv", "w", newline="", encoding="utf-8") as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)

    # 3. XML
    root = ET.Element(table_name)
    for item in data:
        row_el = ET.SubElement(root, "row")
        for key, value in item.items():
            child = ET.SubElement(row_el, key)
            child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(f"out/{table_name}.xml", encoding="utf-8", xml_declaration=True)

    # 4. YAML
    with open(f"out/{table_name}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

    print(f"Данные из таблицы '{table_name}' выгружены в папку out/")
