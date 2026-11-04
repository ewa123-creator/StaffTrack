"""Сервис экспорта данных в форматы JSON, CSV, XML, YAML."""

import os
import csv
import json
import xml.etree.ElementTree as ET
import yaml

from src.repositories import assignment_repo


def export_data():
    # 1. Получаем данные из БД (используем наш JOIN-запрос)
    assignments = assignment_repo.get_all_with_details()

    # 2. Собираем данные в список словарей
    data = []
    for a in assignments:
        data.append({
            "assignment_id": a.assignment_id,
            "employee": {
                "name": a.employee_full_name,
            },
            "position": a.position_title,
            "start_date": a.start_date,
            "end_date": a.end_date or "по наст. время"
        })

    # 3. Создаем папку out, если её нет
    out_dir = "out"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 4. Экспорт в JSON
    with open(os.path.join(out_dir, "data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # 5. Экспорт в CSV
    with open(os.path.join(out_dir, "data.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Сотрудник", "Должность", "Дата начала", "Дата окончания"])
        for item in data:
            writer.writerow([
                item["assignment_id"],
                item["employee"]["name"],
                item["position"],
                item["start_date"],
                item["end_date"]
            ])

    # 6. Экспорт в XML
    root = ET.Element("assignments")
    for item in data:
        assignment_el = ET.SubElement(root, "assignment")
        
        ET.SubElement(assignment_el, "id").text = str(item["assignment_id"])
        
        employee_el = ET.SubElement(assignment_el, "employee")
        ET.SubElement(employee_el, "name").text = item["employee"]["name"]
        
        ET.SubElement(assignment_el, "position").text = item["position"]
        ET.SubElement(assignment_el, "start_date").text = item["start_date"]
        ET.SubElement(assignment_el, "end_date").text = item["end_date"]

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(os.path.join(out_dir, "data.xml"), encoding="utf-8", xml_declaration=True)

    # 7. Экспорт в YAML
    with open(os.path.join(out_dir, "data.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

    print(f"✅ Данные успешно экспортированы в папку '{out_dir}'")
