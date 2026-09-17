# ============================================================
# PYTHON DAY 16
# TOPIC: MODULES, PACKAGES & IMPORTS
# ============================================================

print("===== DAY 16: MODULES, PACKAGES & IMPORTS =====\n")

# A module is a Python file containing reusable code.
# Built-in modules are available with Python; custom modules are files
# that we create ourselves.

# ============================================================
# 1. IMPORTING BUILT-IN MODULES
# ============================================================

print("--- 1. IMPORTING BUILT-IN MODULES ---")

import math
import statistics

print(f"Square root of 81: {math.sqrt(81)}")
print(f"Value of pi: {math.pi:.4f}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Mean: {statistics.mean([10, 20, 30])}")

print()

# ============================================================
# 2. IMPORT WITH AN ALIAS
# ============================================================

print("--- 2. IMPORT ALIAS ---")

import datetime as dt

current_date = dt.date.today()
print(f"Today: {current_date}")
print(f"Year: {current_date.year}")

print()

# ============================================================
# 3. FROM IMPORT
# ============================================================

print("--- 3. FROM IMPORT ---")

from math import ceil, floor, gcd

print(f"ceil(4.2): {ceil(4.2)}")
print(f"floor(4.8): {floor(4.8)}")
print(f"GCD of 48 and 18: {gcd(48, 18)}")

print()

# ============================================================
# 4. RANDOM MODULE
# ============================================================

print("--- 4. RANDOM MODULE ---")

import random

random.seed(7)  # A fixed seed makes this demonstration repeatable.
colors = ["red", "green", "blue", "yellow"]
print(f"Random color: {random.choice(colors)}")
print(f"Random number from 1 to 10: {random.randint(1, 10)}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

print()

# ============================================================
# 5. USEFUL MODULE INFORMATION
# ============================================================

print("--- 5. MODULE INFORMATION ---")

import os
import sys

print(f"Operating system: {os.name}")
print(f"Python major version: {sys.version_info.major}")
print(f"Python minor version: {sys.version_info.minor}")
print(f"Current working directory: {os.getcwd()}")

print()

# ============================================================
# 6. __name__ == '__main__'
# ============================================================

print("--- 6. MAIN GUARD ---")


def greet(name):
    """Return a greeting that could be reused by another module."""
    return f"Hello, {name}!"


# This condition is true when this file is run directly. It is false when
# another file imports this module, which prevents demonstration code from
# running unexpectedly.
if __name__ == "__main__":
    print(greet("Python learner"))

print()

# ============================================================
# 7. CREATING A REUSABLE TOOLKIT
# ============================================================

print("--- 7. REUSABLE TOOLKIT ---")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def is_even(number):
    return number % 2 == 0


def summarize_numbers(values):
    return {
        "count": len(values),
        "total": sum(values),
        "minimum": min(values),
        "maximum": max(values),
        "average": statistics.mean(values),
    }

print(f"20°C in Fahrenheit: {celsius_to_fahrenheit(20):.1f}°F")
print(f"68°F in Celsius: {fahrenheit_to_celsius(68):.1f}°C")
print(f"Is 42 even? {is_even(42)}")
print(f"Summary: {summarize_numbers([5, 10, 15, 20])}")

print()

# ============================================================
# 8. PRACTICAL EXAMPLE: UNIT CONVERTER
# ============================================================

print("--- 8. PRACTICAL EXAMPLE: UNIT CONVERTER ---")


def convert_distance(value, unit):
    """Convert kilometers or miles to both units."""
    if value < 0:
        raise ValueError("Distance cannot be negative")
    if unit == "km":
        kilometers = value
        miles = value * 0.621371
    elif unit == "mi":
        miles = value
        kilometers = value / 0.621371
    else:
        raise ValueError("Unit must be 'km' or 'mi'")
    return {"kilometers": kilometers, "miles": miles}


print(convert_distance(10, "km"))
print(convert_distance(5, "mi"))

print()

# ============================================================
# DAY 16 CHALLENGES
# ============================================================

# Challenge 1: Create a calculator module with add, subtract, multiply, divide.
# Challenge 2: Use the random module to build a number guessing game.
# Challenge 3: Create a temperature_converter.py custom module.
# Challenge 4: Import selected functions instead of importing everything.
# Challenge 5: Add a main guard to a reusable module.
# Challenge 6: Use os to list files in the current directory.
# Challenge 7: Use statistics to create a grade report.
# Challenge 8: Build a package with math_tools and text_tools modules.

print("✓ Day 16 completed!")
