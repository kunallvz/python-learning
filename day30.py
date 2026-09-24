# Day 30 - Python learning
# Practice with dictionaries, tuples, and nested data

student = {
    "name": "Kunal",
    "age": 22,
    "city": "Pune",
    "skills": ["Python", "SQL", "Git"],
    "marks": {"Math": 90, "Science": 85, "English": 88}
}

print("Student details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Access a nested dictionary value
print("Math marks:", student["marks"]["Math"])

# Add a new key
student["grade"] = "A"
print("Updated student:", student)

# Tuple example
point = (10, 20)
print("Point:", point)

# Unpacking tuple
x, y = point
print("x =", x, "y =", y)

# Common dictionary operations
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Name in student:", "name" in student)
