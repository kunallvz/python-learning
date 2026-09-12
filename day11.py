# ============================================================
# PYTHON DAY 11
# TOPIC: DICTIONARIES - ADVANCED OPERATIONS & METHODS
# ============================================================

print("===== DAY 11: DICTIONARIES =====\n")

# ============================================================
# 1. CREATING DICTIONARIES
# ============================================================

print("--- 1. CREATING DICTIONARIES ---")

# Empty dictionary
empty_dict = {}
empty_dict_2 = dict()
print(f"Empty dictionary: {empty_dict}")

# Dictionary with initial values
student = {"name": "Kunal", "age": 20, "city": "Delhi"}
print(f"Student: {student}")

# Dictionary with different data types
mixed_dict = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6)
}
print(f"Mixed dictionary: {mixed_dict}")

print()

# ============================================================
# 2. ACCESSING DICTIONARY VALUES
# ============================================================

print("--- 2. ACCESSING DICTIONARY VALUES ---")

person = {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"}

# Using keys to access values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using .get() method (safer - returns None if key doesn't exist)
print(f"Job: {person.get('job')}")
print(f"Country (doesn't exist): {person.get('country')}")
print(f"Country with default: {person.get('country', 'Not specified')}")

print()

# ============================================================
# 3. ADDING & MODIFYING VALUES
# ============================================================

print("--- 3. ADDING & MODIFYING VALUES ---")

book = {"title": "Python Basics", "author": "John", "year": 2020}
print(f"Original: {book}")

# Add new key-value pair
book["price"] = 499
print(f"After adding price: {book}")

# Modify existing value
book["year"] = 2024
print(f"After updating year: {book}")

# Add multiple values at once
book.update({"publisher": "Tech Press", "pages": 350})
print(f"After update(): {book}")

print()

# ============================================================
# 4. REMOVING VALUES FROM DICTIONARY
# ============================================================

print("--- 4. REMOVING VALUES FROM DICTIONARY ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2023, "color": "Blue"}
print(f"Original: {car}")

# Using del keyword
del car["color"]
print(f"After del car['color']: {car}")

# Using pop() - removes and returns the value
year = car.pop("year")
print(f"Popped year: {year}")
print(f"After pop(): {car}")

# Using pop() with default value if key doesn't exist
transmission = car.pop("transmission", "Manual")
print(f"Transmission (default): {transmission}")

# Using popitem() - removes last inserted item
item = car.popitem()
print(f"Popitem removed: {item}")
print(f"After popitem(): {car}")

# Using clear() - removes all items
demo = {"a": 1, "b": 2}
demo.clear()
print(f"After clear(): {demo}")

print()

# ============================================================
# 5. DICTIONARY KEYS, VALUES, ITEMS
# ============================================================

print("--- 5. DICTIONARY KEYS, VALUES, ITEMS ---")

movie = {"title": "Inception", "director": "Nolan", "year": 2010, "rating": 8.8}

# Get all keys
keys = movie.keys()
print(f"Keys: {keys}")
print(f"Keys as list: {list(keys)}")

# Get all values
values = movie.values()
print(f"Values: {values}")
print(f"Values as list: {list(values)}")

# Get key-value pairs
items = movie.items()
print(f"Items: {items}")
print(f"Items as list: {list(items)}")

print()

# ============================================================
# 6. ITERATING THROUGH DICTIONARIES
# ============================================================

print("--- 6. ITERATING THROUGH DICTIONARIES ---")

employee = {"id": 101, "name": "Raj", "position": "Developer", "salary": 50000}

# Iterate through keys
print("Iterating through keys:")
for key in employee:
    print(f"  {key}")

# Iterate through values
print("Iterating through values:")
for value in employee.values():
    print(f"  {value}")

# Iterate through key-value pairs
print("Iterating through items:")
for key, value in employee.items():
    print(f"  {key}: {value}")

print()

# ============================================================
# 7. CHECKING IF KEY EXISTS
# ============================================================

print("--- 7. CHECKING IF KEY EXISTS ---")

product = {"name": "Laptop", "price": 80000, "stock": 15}

# Using 'in' operator
if "name" in product:
    print("'name' key exists")

if "brand" in product:
    print("'brand' key exists")
else:
    print("'brand' key does not exist")

# Using 'not in' operator
if "discount" not in product:
    print("'discount' key not in product")

print()

# ============================================================
# 8. DICTIONARY LENGTH & MEMBERSHIP
# ============================================================

print("--- 8. DICTIONARY LENGTH & MEMBERSHIP ---")

scores = {"math": 95, "english": 87, "science": 92, "history": 85}

# Length of dictionary
print(f"Number of subjects: {len(scores)}")

# Check if value exists
if 95 in scores.values():
    print("Score of 95 exists in the dictionary")

# Find key by value
for key, value in scores.items():
    if value == 92:
        print(f"Science score is 92")

print()

# ============================================================
# 9. COPYING DICTIONARIES
# ============================================================

print("--- 9. COPYING DICTIONARIES ---")

original = {"a": 1, "b": 2, "c": 3}

# Shallow copy using copy()
shallow_copy = original.copy()
shallow_copy["a"] = 100
print(f"Original: {original}")
print(f"Shallow copy after modification: {shallow_copy}")

# Assignment (both reference same dictionary)
reference = original
reference["x"] = 10
print(f"Original after reference modification: {original}")

print()

# ============================================================
# 10. NESTED DICTIONARIES
# ============================================================

print("--- 10. NESTED DICTIONARIES ---")

company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "John", "dept": "IT"},
        "emp2": {"name": "Sarah", "dept": "HR"},
        "emp3": {"name": "Mike", "dept": "Sales"}
    },
    "location": "New York"
}

print(f"Company: {company['name']}")
print(f"First employee: {company['employees']['emp1']}")
print(f"First employee name: {company['employees']['emp1']['name']}")

# Iterate nested dictionary
print("All employees:")
for emp_id, emp_info in company["employees"].items():
    print(f"  {emp_id}: {emp_info['name']} - {emp_info['dept']}")

print()

# ============================================================
# 11. MERGING DICTIONARIES
# ============================================================

print("--- 11. MERGING DICTIONARIES ---")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Method 1: Using update()
merged1 = dict1.copy()
merged1.update(dict2)
merged1.update(dict3)
print(f"Merged (using update): {merged1}")

# Method 2: Using ** operator (Python 3.9+)
merged2 = {**dict1, **dict2, **dict3}
print(f"Merged (using **): {merged2}")

# Method 3: Using | operator (Python 3.9+)
merged3 = dict1 | dict2 | dict3
print(f"Merged (using |): {merged3}")

print()

# ============================================================
# 12. DICTIONARY COMPREHENSION
# ============================================================

print("--- 12. DICTIONARY COMPREHENSION ---")

# Create dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create dictionary from lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(f"People: {people}")

# Create dictionary with condition
numbers = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print(f"Numbers: {numbers}")

print()

# ============================================================
# 13. DICTIONARY METHODS
# ============================================================

print("--- 13. DICTIONARY METHODS ---")

config = {"host": "localhost", "port": 8000, "debug": True}

# setdefault() - returns value if key exists, else adds key with default value
timeout = config.setdefault("timeout", 30)
print(f"Timeout: {timeout}")
print(f"Config after setdefault: {config}")

# fromkeys() - create dictionary with same value for all keys
keys = ["name", "email", "phone"]
template = dict.fromkeys(keys, "N/A")
print(f"Template: {template}")

print()

# ============================================================
# 14. SORTING DICTIONARY
# ============================================================

print("--- 14. SORTING DICTIONARY ---")

marks = {"Alice": 95, "Charlie": 87, "Bob": 92, "Diana": 88}

# Sort by keys
sorted_by_keys = dict(sorted(marks.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# Sort by values
sorted_by_values = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by values (descending): {sorted_by_values}")

print()

# ============================================================
# MINI PROJECT 1: STUDENT MANAGEMENT SYSTEM
# ============================================================

print("--- MINI PROJECT 1: STUDENT MANAGEMENT ---")

students = {
    "S001": {"name": "Kunal", "marks": [85, 90, 88]},
    "S002": {"name": "Priya", "marks": [92, 88, 95]},
    "S003": {"name": "Arjun", "marks": [78, 82, 80]}
}

# Calculate average for each student
for sid, student_data in students.items():
    avg = sum(student_data["marks"]) / len(student_data["marks"])
    print(f"{student_data['name']}: {avg:.2f}")

print()

# ============================================================
# MINI PROJECT 2: PHONE DIRECTORY
# ============================================================

print("--- MINI PROJECT 2: PHONE DIRECTORY ---")

directory = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098",
    "Diana": "6543210987"
}

def search_contact(name):
    """Search for contact in directory"""
    return directory.get(name, "Contact not found")

def add_contact(name, phone):
    """Add new contact"""
    if name in directory:
        print(f"{name} already exists!")
    else:
        directory[name] = phone
        print(f"{name} added successfully!")

# Search
print(f"Alice's number: {search_contact('Alice')}")
print(f"Eve's number: {search_contact('Eve')}")

# Add
add_contact("Eve", "5432109876")
print(f"After adding Eve: {directory}")

print()

# ============================================================
# DAY 11 CHALLENGES
# ============================================================

# Challenge 1
# Create a dictionary of 5 countries with their capitals
# Print each country and capital

# Challenge 2
# Create a dictionary of students with their marks
# Find the student with highest marks

# Challenge 3
# Create a nested dictionary for a library with books
# Access and print specific book information

# Challenge 4
# Merge two dictionaries without using update()

# Challenge 5
# Count frequency of characters in a string using dictionary
# Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Challenge 6
# Create a function that converts list of tuples to dictionary
# Example: [('a', 1), ('b', 2)] -> {'a': 1, 'b': 2}

# Challenge 7
# Create a dictionary that stores user information
# Add method to update user info
# Add method to delete user

# Challenge 8
# Create a dictionary with default values using setdefault()
# Handle missing keys gracefully

# ============================================================
# DAY 11 GOAL
# ============================================================

# By the end of Day 11, you should understand:
#
# • Creating dictionaries
# • Accessing values using keys
# • Adding and modifying values
# • Removing values (del, pop, popitem, clear)
# • Dictionary methods (keys, values, items)
# • Iterating through dictionaries
# • Checking key existence
# • Copying dictionaries (shallow vs reference)
# • Nested dictionaries
# • Merging dictionaries
# • Dictionary comprehension
# • Dictionary methods (get, setdefault, fromkeys)
# • Sorting dictionaries
#
# MOST IMPORTANT:
# Don't just copy the code.
# Modify it and create your own dictionaries.
# Practice with real-world examples (student records, phone directory)
# Understand the difference between .get() and direct access with []
