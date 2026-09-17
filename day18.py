# ============================================================
# PYTHON DAY 18
# TOPIC: JSON AND CSV DATA
# ============================================================

print("===== DAY 18: JSON AND CSV DATA =====\n")

import csv
import json
from pathlib import Path

# JSON is useful for structured data. CSV is useful for rows and columns.

# ============================================================
# 1. PYTHON DATA TO JSON TEXT
# ============================================================

print("--- 1. PYTHON DATA TO JSON TEXT ---")

profile = {
    "name": "Kunal",
    "age": 20,
    "skills": ["Python", "GitHub", "Problem Solving"],
    "is_learning": True,
}

json_text = json.dumps(profile, indent=4)
print(json_text)

print()

# ============================================================
# 2. JSON TEXT TO PYTHON DATA
# ============================================================

print("--- 2. JSON TEXT TO PYTHON DATA ---")

loaded_profile = json.loads(json_text)
print(f"Name: {loaded_profile['name']}")
print(f"First skill: {loaded_profile['skills'][0]}")
print(f"Learning: {loaded_profile['is_learning']}")

print()

# ============================================================
# 3. WRITING JSON TO A FILE
# ============================================================

print("--- 3. WRITING JSON FILE ---")

settings = {
    "theme": "dark",
    "font_size": 16,
    "notifications": True,
    "recent_topics": ["functions", "classes", "exceptions"],
}

settings_path = Path("day18_settings.json")
with settings_path.open("w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)

print(f"Saved data to {settings_path}")

# ============================================================
# 4. READING JSON FROM A FILE
# ============================================================

print("--- 4. READING JSON FILE ---")

with settings_path.open("r", encoding="utf-8") as file:
    saved_settings = json.load(file)

for key, value in saved_settings.items():
    print(f"{key}: {value}")

print()

# ============================================================
# 5. UPDATING JSON DATA
# ============================================================

print("--- 5. UPDATING JSON DATA ---")

saved_settings["font_size"] = 18
saved_settings["recent_topics"].append("file handling")

with settings_path.open("w", encoding="utf-8") as file:
    json.dump(saved_settings, file, indent=4)

print("Settings updated successfully.")

print()

# ============================================================
# 6. SAFE JSON PARSING
# ============================================================

print("--- 6. SAFE JSON PARSING ---")


def parse_json_safely(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error.msg}")
        return None


print(parse_json_safely('{"name": "Asha", "score": 95}'))
print(parse_json_safely('{"name": "Asha", "score": }'))

print()

# ============================================================
# 7. WRITING CSV DATA
# ============================================================

print("--- 7. WRITING CSV DATA ---")

students = [
    {"name": "Asha", "course": "Python", "score": 92},
    {"name": "Ravi", "course": "Python", "score": 85},
    {"name": "Mina", "course": "Python", "score": 96},
]

students_path = Path("day18_students.csv")
fieldnames = ["name", "course", "score"]

with students_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print(f"Saved {len(students)} students to {students_path}")

# ============================================================
# 8. READING CSV DATA
# ============================================================

print("--- 8. READING CSV DATA ---")

with students_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    loaded_students = list(reader)

for student in loaded_students:
    print(f"{student['name']}: {student['score']}/100")

scores = [int(student["score"]) for student in loaded_students]
print(f"Average score: {sum(scores) / len(scores):.2f}")

print()

# ============================================================
# 9. PRACTICAL EXAMPLE: JSON TASK MANAGER
# ============================================================

print("--- 9. PRACTICAL EXAMPLE: JSON TASK MANAGER ---")


def add_task(tasks, title, priority="medium"):
    tasks.append({"title": title, "priority": priority, "completed": False})


def complete_task(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            return True
    return False


def show_tasks(tasks):
    for number, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{number}. [{status}] {task['title']} ({task['priority']})")


tasks = []
add_task(tasks, "Practice JSON", "high")
add_task(tasks, "Build a CSV report")
complete_task(tasks, "Practice JSON")
show_tasks(tasks)

print()

# ============================================================
# DAY 18 CHALLENGES
# ============================================================

# Challenge 1: Save a list of books as JSON.
# Challenge 2: Load JSON and find all books by a selected author.
# Challenge 3: Build a CSV expense tracker.
# Challenge 4: Convert CSV data into JSON data.
# Challenge 5: Validate required JSON keys before using them.
# Challenge 6: Add delete and search operations to the task manager.
# Challenge 7: Calculate category totals from an expense CSV.
# Challenge 8: Create a JSON-backed student grade application.

print("✓ Day 18 completed!")
