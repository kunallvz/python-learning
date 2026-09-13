# ============================================================
# PYTHON DAY 12
# TOPIC: FUNCTIONS & LAMBDA EXPRESSIONS
# ============================================================

print("===== DAY 12: FUNCTIONS & LAMBDA =====\n")

# ============================================================
# 1. BASIC FUNCTION DEFINITION
# ============================================================

print("--- 1. BASIC FUNCTION DEFINITION ---")

def greet():
    """Simple function that greets"""
    print("Hello, Welcome to Python!")

greet()

# Function with parameters
def add(a, b):
    """Function to add two numbers"""
    print(f"{a} + {b} = {a + b}")
    return a + b

result = add(5, 3)
print(f"Result: {result}")

print()

# ============================================================
# 2. FUNCTION PARAMETERS
# ============================================================

print("--- 2. FUNCTION PARAMETERS ---")

# Positional parameters
def subtract(x, y):
    return x - y

print(f"10 - 3 = {subtract(10, 3)}")

# Default parameters
def power(base, exponent=2):
    """Calculate power with default exponent 2"""
    return base ** exponent

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")

# Keyword arguments
def describe_person(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

describe_person(name="Kunal", age=20, city="Delhi")
describe_person("Priya", "New York", 25)  # Positional

print()

# ============================================================
# 3. VARIABLE LENGTH ARGUMENTS (*args)
# ============================================================

print("--- 3. VARIABLE LENGTH ARGUMENTS (*args) ---")

def sum_numbers(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_numbers(1, 2, 3, 4, 5)}")
print(f"Sum of 10: {sum_numbers(10)}")

# Function with both regular and *args
def print_info(name, *hobbies):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")
    for hobby in hobbies:
        print(f"  - {hobby}")

print_info("Alice", "Reading", "Gaming", "Cooking")

print()

# ============================================================
# 4. KEYWORD ARGUMENTS (**kwargs)
# ============================================================

print("--- 4. KEYWORD ARGUMENTS (**kwargs) ---")

def print_config(**kwargs):
    """Print configuration from keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Server Configuration:")
print_config(host="localhost", port=8000, debug=True, database="postgres")

# Combined: regular args, *args, **kwargs
def full_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

print("\nFull function example:")
full_function(1, 2, 3, 4, 5, name="Kunal", age=20, city="Delhi")

print()

# ============================================================
# 5. RETURN MULTIPLE VALUES
# ============================================================

print("--- 5. RETURN MULTIPLE VALUES ---")

def calculate(x, y):
    """Return sum and product"""
    return x + y, x * y

sum_val, prod_val = calculate(5, 3)
print(f"Sum: {sum_val}, Product: {prod_val}")

# Return as dictionary
def get_user_info():
    return {
        "name": "Kunal",
        "age": 20,
        "email": "kunal@example.com"
    }

user = get_user_info()
print(f"User: {user}")

print()

# ============================================================
# 6. LAMBDA FUNCTIONS
# ============================================================

print("--- 6. LAMBDA FUNCTIONS ---")

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add_lambda = lambda x, y: x + y
print(f"3 + 4 using lambda: {add_lambda(3, 4)}")

# Lambda with conditional
max_val = lambda x, y: x if x > y else y
print(f"Max of 10 and 20: {max_val(10, 20)}")

# Lambda in list
numbers = [1, 2, 3, 4, 5]
squares_lambda = [lambda x=x: x**2 for x in numbers]
print(f"Squares: {[f() for f in squares_lambda]}")

print()

# ============================================================
# 7. MAP FUNCTION
# ============================================================

print("--- 7. MAP FUNCTION ---")

# Map with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# Map with regular function
def convert_celsius(c):
    return (c * 9/5) + 32

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(convert_celsius, celsius_temps))
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")

# Map on multiple lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
multiplied = list(map(lambda x, y: x * y, list1, list2))
print(f"Multiplied: {multiplied}")

print()

# ============================================================
# 8. FILTER FUNCTION
# ============================================================

print("--- 8. FILTER FUNCTION ---")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {evens}")

# Filter with function
def is_positive(x):
    return x > 0

values = [-5, -2, 0, 3, 7, -1, 4]
positive = list(filter(is_positive, values))
print(f"Values: {values}")
print(f"Positive: {positive}")

# Filter strings
words = ["apple", "a", "banana", "cat", "elephant"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(f"Words: {words}")
print(f"Words with length > 3: {long_words}")

print()

# ============================================================
# 9. REDUCE FUNCTION
# ============================================================

print("--- 9. REDUCE FUNCTION ---")

from functools import reduce

# Sum using reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum using reduce: {total}")

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product using reduce: {product}")

# Concatenate strings
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Concatenated: {sentence}")

print()

# ============================================================
# 10. NESTED FUNCTIONS & CLOSURES
# ============================================================

print("--- 10. NESTED FUNCTIONS & CLOSURES ---")

def outer_function(x):
    """Outer function"""
    def inner_function(y):
        """Inner function"""
        return x + y
    return inner_function

add_5 = outer_function(5)
print(f"outer_function(5)(3) = {add_5(3)}")
print(f"outer_function(10)(7) = {outer_function(10)(7)}")

# Closure example
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiply_by_3 = make_multiplier(3)
multiply_by_5 = make_multiplier(5)

print(f"multiply_by_3(10) = {multiply_by_3(10)}")
print(f"multiply_by_5(10) = {multiply_by_5(10)}")

print()

# ============================================================
# 11. DECORATORS (INTRO)
# ============================================================

print("--- 11. DECORATORS (INTRO) ---")

def my_decorator(func):
    def wrapper():
        print("Something before function call")
        func()
        print("Something after function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print()

# ============================================================
# 12. SCOPE: LOCAL VS GLOBAL
# ============================================================

print("--- 12. SCOPE: LOCAL VS GLOBAL ---")

global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(f"Local: {local_var}")
    print(f"Global: {global_var}")

scope_example()
print(f"Global outside function: {global_var}")

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"Counter: {increment()}")
print(f"Counter: {increment()}")
print(f"Counter: {increment()}")

print()

# ============================================================
# 13. DOCSTRINGS & HELP
# ============================================================

print("--- 13. DOCSTRINGS & HELP ---")

def complex_function(a, b):
    """
    This function calculates sum and product of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: (sum, product)
    """
    return a + b, a * b

print(complex_function.__doc__)
help(complex_function)

print()

# ============================================================
# MINI PROJECT: CALCULATOR WITH LAMBDA
# ============================================================

print("--- MINI PROJECT: CALCULATOR WITH LAMBDA ---")

calculator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print(f"5 + 3 = {calculator['+'](5, 3)}")
print(f"10 - 4 = {calculator['-'](10, 4)}")
print(f"6 * 7 = {calculator['*'](6, 7)}")
print(f"20 / 4 = {calculator['/'](20, 4)}")
print(f"20 / 0 = {calculator['/'](20, 0)}")

print()

# ============================================================
# DAY 12 CHALLENGES
# ============================================================

# Challenge 1: Create a function that returns factorial
# Challenge 2: Create a function with *args to find max value
# Challenge 3: Use map to convert a list of strings to integers
# Challenge 4: Use filter to get numbers divisible by 3
# Challenge 5: Create a function that returns a function
# Challenge 6: Use lambda to sort a list of tuples
# Challenge 7: Create a decorator that prints execution time
# Challenge 8: Create a function that calculates area of shapes

print("✓ Day 12 completed!")
