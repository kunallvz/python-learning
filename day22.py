# ============================================================
# PYTHON DAY 22
# TOPIC: FUNCTIONS & REUSABLE CODE
# ============================================================

print("===== DAY 22: FUNCTIONS =====\n")

# Function with parameters

def greet(name):
    return f"Hello, {name}!"

print(greet("Kunal"))
print(greet("Python"))

# Function with default parameter

def add(a, b=5):
    return a + b

print("\nAddition result:", add(10))
print("Addition result:", add(10, 20))

# Function that checks even/odd

def is_even(number):
    return number % 2 == 0

print("Is 12 even?", is_even(12))
print("Is 15 even?", is_even(15))

# Function with multiple returns

def min_max(values):
    return min(values), max(values)

numbers = [4, 7, 2, 9, 1]
minimum, maximum = min_max(numbers)
print("Min:", minimum)
print("Max:", maximum)

# Calculator function

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"

print("Calculator add:", calculator(8, 3, "add"))
print("Calculator div:", calculator(10, 2, "div"))

print("\n✓ Day 22 completed!")
