# Day 31 - Python learning
# Practice with functions, arguments, and return values

def greet(name):
    return f"Hello, {name}! Welcome to Python learning."


def add(a, b):
    return a + b


def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def student_summary(name, age, country="India"):
    return {
        "name": name,
        "age": age,
        "country": country,
    }


print(greet("Kunal"))
print("Sum:", add(12, 8))
print("Product:", multiply(2, 3, 4, 5))
print(student_summary("Aditi", 21))
print(student_summary("Rahul", 25, "USA"))

# Function with default return

def is_even(number):
    if number % 2 == 0:
        return True
    return False

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
