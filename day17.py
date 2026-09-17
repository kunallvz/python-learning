# ============================================================
# PYTHON DAY 17
# TOPIC: FILE HANDLING
# ============================================================

print("===== DAY 17: FILE HANDLING =====\n")

# File modes:
# r = read, w = write, a = append, x = create
# Always prefer `with open(...)` because it closes the file automatically.

FILE_NAME = "day17_notes.txt"

# ============================================================
# 1. WRITING TEXT TO A FILE
# ============================================================

print("--- 1. WRITING TEXT ---")

with open(FILE_NAME, "w", encoding="utf-8") as file:
    file.write("Python file handling\n")
    file.write("Writing text is easy with the write() method.\n")
    file.write("This file was created during Day 17.\n")

print(f"Created {FILE_NAME}")

print()

# ============================================================
# 2. READING THE COMPLETE FILE
# ============================================================

print("--- 2. READING THE COMPLETE FILE ---")

with open(FILE_NAME, "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# ============================================================
# 3. READING LINE BY LINE
# ============================================================

print("--- 3. READING LINE BY LINE ---")

with open(FILE_NAME, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")

print()

# ============================================================
# 4. READLINES AND STRIP
# ============================================================

print("--- 4. READLINES ---")

with open(FILE_NAME, "r", encoding="utf-8") as file:
    lines = file.readlines()

clean_lines = [line.strip() for line in lines if line.strip()]
print(f"Number of non-empty lines: {len(clean_lines)}")
print(f"Lines: {clean_lines}")

print()

# ============================================================
# 5. APPENDING TO A FILE
# ============================================================

print("--- 5. APPENDING ---")

with open(FILE_NAME, "a", encoding="utf-8") as file:
    file.write("A new line was appended later.\n")

with open(FILE_NAME, "r", encoding="utf-8") as file:
    print(file.read())

# ============================================================
# 6. FILE INFORMATION
# ============================================================

print("--- 6. FILE INFORMATION ---")

import os

print(f"Exists: {os.path.exists(FILE_NAME)}")
print(f"Is a file: {os.path.isfile(FILE_NAME)}")
print(f"Size: {os.path.getsize(FILE_NAME)} bytes")

print()

# ============================================================
# 7. SAFE FILE READING
# ============================================================

print("--- 7. SAFE FILE READING ---")


def read_file_safely(filename):
    """Read a file and return a friendly message for common errors."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"The file '{filename}' does not exist."
    except PermissionError:
        return f"Permission denied while reading '{filename}'."
    except OSError as error:
        return f"Could not read the file: {error}"


print(read_file_safely(FILE_NAME))
print(read_file_safely("does_not_exist.txt"))

print()

# ============================================================
# 8. CSV-LIKE DATA WITH TEXT FILES
# ============================================================

print("--- 8. CSV-LIKE DATA ---")

students_file = "day17_students.csv"

with open(students_file, "w", encoding="utf-8") as file:
    file.write("name,course,score\n")
    file.write("Asha,Python,92\n")
    file.write("Ravi,Python,85\n")
    file.write("Mina,Python,96\n")

with open(students_file, "r", encoding="utf-8") as file:
    rows = file.read().splitlines()

header = rows[0].split(",")
print(f"Columns: {header}")
for row in rows[1:]:
    name, course, score = row.split(",")
    print(f"{name} scored {score} in {course}")

print()

# ============================================================
# 9. PRACTICAL EXAMPLE: LOG FILE
# ============================================================

print("--- 9. PRACTICAL EXAMPLE: LOG FILE ---")

log_file = "day17_app.log"


def write_log(message, filename=log_file):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"LOG: {message}\n")


write_log("Application started")
write_log("User opened the dashboard")
write_log("Application finished")

print(read_file_safely(log_file))

print()

# ============================================================
# DAY 17 CHALLENGES
# ============================================================

# Challenge 1: Build a note-taking program that appends notes to a file.
# Challenge 2: Count words, lines, and characters in a text file.
# Challenge 3: Copy one file into another file.
# Challenge 4: Create a contact book stored in a text file.
# Challenge 5: Search for a word in every line of a file.
# Challenge 6: Read a CSV file and calculate the average score.
# Challenge 7: Build a simple log analyzer.
# Challenge 8: Handle missing files and invalid permissions gracefully.

print("✓ Day 17 completed!")
