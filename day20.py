# ============================================================
# PYTHON DAY 20
# TOPIC: LISTS, TUPLES, SETS & DICTIONARIES
# ============================================================

print("===== DAY 20: DATA STRUCTURES =====\n")

# Lists
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("Slice:", numbers[1:4])

numbers.append(60)
numbers.insert(2, 25)
print("Updated list:", numbers)
print("Sorted list:", sorted(numbers))

# Tuples
point = (5, 10)
print("Tuple:", point)
print("Tuple item:", point[1])

# Sets
unique_numbers = {10, 20, 20, 30, 40}
print("Set:", unique_numbers)
print("Union:", {1, 2, 3} | {3, 4, 5})

# Dictionaries
student = {
    "name": "Kunal",
    "age": 22,
    "city": "Pune",
    "skills": ["Python", "SQL", "Git"]
}
print("Dictionary:", student)
print("Name:", student["name"])
print("Skills:", ", ".join(student["skills"]))

# Practice task
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
print("Top score:", max(scores.values()))
print("Student names:", list(scores.keys()))

print("\n✓ Day 20 completed!")
