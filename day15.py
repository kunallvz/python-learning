# ============================================================
# PYTHON DAY 15
# TOPIC: EXCEPTION HANDLING & ERROR MANAGEMENT
# ============================================================

print("===== DAY 15: EXCEPTION HANDLING =====\n")

# ============================================================
# 1. TRY-EXCEPT BASICS
# ============================================================

print("--- 1. TRY-EXCEPT BASICS ---")

# Example 1: Catching ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    result = 0

print(f"Result: {result}")

# Example 2: Catching ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format!")
    number = 0

print(f"Number: {number}")

print()

# ============================================================
# 2. MULTIPLE EXCEPTION HANDLERS
# ============================================================

print("--- 2. MULTIPLE EXCEPTION HANDLERS ---")

try:
    numbers = [1, 2, 3]
    print(f"Element at index 5: {numbers[5]}")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Value error!")

print()

try:
    result = int("xyz") / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid number format!")

print()

# ============================================================
# 3. GENERIC EXCEPTION HANDLER
# ============================================================

print("--- 3. GENERIC EXCEPTION HANDLER ---")

try:
    data = {"name": "Kunal"}
    print(data["age"])  # KeyError
except Exception as e:
    print(f"An error occurred: {type(e).__name__}")
    print(f"Error message: {e}")

print()

# ============================================================
# 4. ELSE CLAUSE
# ============================================================

print("--- 4. ELSE CLAUSE ---")

try:
    num = int(input("Enter a number (or press Enter to use default): ") or "10")
    result = 20 / num
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Division successful: 20 / {num} = {result}")

print()

# ============================================================
# 5. FINALLY CLAUSE
# ============================================================

print("--- 5. FINALLY CLAUSE ---")

try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File read successfully")
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Finally block always executes")
    if 'file' in locals():
        file.close()

print()

# ============================================================
# 6. RAISING EXCEPTIONS
# ============================================================

print("--- 6. RAISING EXCEPTIONS ---")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot exceed 150!")
    return True

try:
    validate_age(25)
    print("Age is valid!")
except ValueError as e:
    print(f"Error: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

print()

# ============================================================
# 7. CUSTOM EXCEPTIONS
# ============================================================

print("--- 7. CUSTOM EXCEPTIONS ---")

class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid amount"""
    pass

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive!")
        if amount > self.balance:
            raise InsufficientBalanceError(f"Insufficient balance! Available: ${self.balance}")
        self.balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${self.balance}")

account = BankAccount("Kunal", 1000)

try:
    account.withdraw(500)
except (InvalidAmountError, InsufficientBalanceError) as e:
    print(f"Error: {e}")

try:
    account.withdraw(1000)  # More than available
except (InvalidAmountError, InsufficientBalanceError) as e:
    print(f"Error: {e}")

print()

# ============================================================
# 8. TRACEBACK AND DEBUGGING
# ============================================================

print("--- 8. TRACEBACK AND DEBUGGING ---")

import traceback

def divide(x, y):
    return x / y

def calculate():
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        print("Full traceback:")
        traceback.print_exc()
        print("\nSimple error message:")
        print(f"Error: Cannot divide by zero!")

calculate()

print()

# ============================================================
# 9. CONTEXT MANAGERS (WITH STATEMENT)
# ============================================================

print("--- 9. CONTEXT MANAGERS (WITH STATEMENT) ---")

# Writing to file safely
try:
    with open('demo.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is Day 15 - Exception Handling\n")
    print("File written successfully!")
except IOError as e:
    print(f"Error writing file: {e}")

# Reading from file safely
try:
    with open('demo.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found!")

print()

# ============================================================
# 10. EXCEPTION HANDLING IN FUNCTIONS
# ============================================================

print("--- 10. EXCEPTION HANDLING IN FUNCTIONS ---")

def process_list(items, index):
    """Process list item at given index"""
    try:
        if not isinstance(items, list):
            raise TypeError("First argument must be a list!")
        if not isinstance(index, int):
            raise TypeError("Index must be an integer!")
        if index < 0 or index >= len(items):
            raise IndexError(f"Index {index} out of range!")
        return items[index]
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")
        return None

# Test function
data = [10, 20, 30, 40, 50]
print(f"Element at index 2: {process_list(data, 2)}")
print(f"Element at index 10: {process_list(data, 10)}")
print(f"Element (invalid type): {process_list(data, 'a')}")

print()

# ============================================================
# 11. ASSERTION AND TESTING
# ============================================================

print("--- 11. ASSERTION AND TESTING ---")

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    assert price > 0, "Price must be positive!"
    assert 0 <= discount_percent <= 100, "Discount must be between 0 and 100!"
    return price * (1 - discount_percent / 100)

try:
    print(f"Discounted price: ${calculate_discount(100, 20)}")
    print(f"Discounted price: ${calculate_discount(-100, 20)}")  # Will fail
except AssertionError as e:
    print(f"Assertion Error: {e}")

print()

# ============================================================
# 12. PRACTICAL EXAMPLE: SAFE USER INPUT
# ============================================================

print("--- 12. PRACTICAL EXAMPLE: SAFE USER INPUT ---")

def get_integer(prompt, min_val=None, max_val=None):
    """Get valid integer from user"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Value must be >= {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Value must be <= {max_val}")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Simulating user input for demonstration
print("(Simulated: entering 25 for age)")
# age = get_integer("Enter your age: ", 0, 150)
# print(f"Your age: {age}")

print()

# ============================================================
# 13. EXCEPTION HIERARCHY
# ============================================================

print("--- 13. EXCEPTION HIERARCHY ---")

print("Python Exception Hierarchy:")
print("""
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── ImportError
    ├── KeyError
    ├── NameError
    ├── TypeError
    ├── ValueError
    └── ... and many more
""")

print()

# ============================================================
# 14. PRACTICAL EXAMPLE: CALCULATOR WITH FULL ERROR HANDLING
# ============================================================

print("--- 14. PRACTICAL EXAMPLE: CALCULATOR ---")

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, x, y):
        try:
            result = x + y
            self.history.append(f"{x} + {y} = {result}")
            return result
        except TypeError as e:
            print(f"Error: Invalid operands - {e}")
            return None
    
    def divide(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = x / y
            self.history.append(f"{x} / {y} = {result}")
            return result
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            return None
    
    def show_history(self):
        print("Calculation History:")
        for operation in self.history:
            print(f"  {operation}")

calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 / 2 = {calc.divide(10, 2)}")
print(f"10 / 0 = {calc.divide(10, 0)}")
calc.show_history()

print()

# ============================================================
# DAY 15 CHALLENGES
# ============================================================

# Challenge 1: Create a function that validates email format
# Challenge 2: Create a function that safely reads a file
# Challenge 3: Create a custom exception for age validation
# Challenge 4: Build a simple calculator with error handling
# Challenge 5: Create a function that parses JSON safely
# Challenge 6: Build a database connection handler with retry logic
# Challenge 7: Create a data validator class
# Challenge 8: Build a complete error logging system

print("✓ Day 15 completed!")
print("✓ ===== ALL 4 COMMITS COMPLETED! =====")
print("✓ Days 12, 13, 14, 15 are now ready!")
