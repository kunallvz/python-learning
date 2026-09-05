# ============================================================
# PYTHON DAY 5
# TOPIC: FUNCTIONS
# ============================================================


# ------------------------------------------------------------
# 1. BASIC FUNCTION
# ------------------------------------------------------------

def hello():
    print("Hello, Python!")


hello()


# ------------------------------------------------------------
# 2. FUNCTION WITH PARAMETER
# ------------------------------------------------------------

def greet(name):
    print("Hello", name)


greet("Kunal")
greet("Python")


# ------------------------------------------------------------
# 3. MULTIPLE PARAMETERS
# ------------------------------------------------------------

def add(a, b):
    return a + b


result = add(10, 20)
print("Result:", result)


# ------------------------------------------------------------
# 4. RETURN
# ------------------------------------------------------------

def square(number):
    return number * number


x = square(5)
print("Square:", x)


# ------------------------------------------------------------
# 5. IF/ELSE INSIDE FUNCTION
# ------------------------------------------------------------

def check_age(age):

    if age >= 18:
        return "Adult"
    else:
        return "Minor"


print(check_age(20))
print(check_age(15))


# ------------------------------------------------------------
# 6. EVEN OR ODD
# ------------------------------------------------------------

def even_or_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(10))
print(even_or_odd(7))


# ------------------------------------------------------------
# 7. DEFAULT PARAMETER
# ------------------------------------------------------------

def welcome(name="User"):
    print("Welcome", name)


welcome("Kunal")
welcome()


# ------------------------------------------------------------
# 8. FUNCTION + LOOP
# ------------------------------------------------------------

def multiplication_table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


multiplication_table(5)


# ------------------------------------------------------------
# 9. FUNCTION + LIST
# ------------------------------------------------------------

def print_fruits(fruits):

    for fruit in fruits:
        print(fruit)


my_fruits = ["Apple", "Mango", "Banana"]

print_fruits(my_fruits)


# ------------------------------------------------------------
# 10. SUM OF LIST
# ------------------------------------------------------------

def list_sum(numbers):

    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 20, 30, 40]

print("Total:", list_sum(numbers))


# ------------------------------------------------------------
# 11. FIND LARGEST NUMBER
# ------------------------------------------------------------

def find_largest(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


numbers = [10, 50, 20, 80, 30]

print("Largest:", find_largest(numbers))


# ------------------------------------------------------------
# 12. COUNT EVEN NUMBERS
# ------------------------------------------------------------

def count_even(numbers):

    count = 0

    for number in numbers:

        if number % 2 == 0:
            count = count + 1

    return count


numbers = [1, 2, 3, 4, 5, 6]

print("Even numbers:", count_even(numbers))


# ------------------------------------------------------------
# 13. LOCAL VARIABLE
# ------------------------------------------------------------

def test():

    message = "Hello"

    print(message)


test()

# 'message' only exists inside test()
# print(message)  # This would cause an error


# ------------------------------------------------------------
# 14. FUNCTION USING USER INPUT
# ------------------------------------------------------------

def user_greeting():

    name = input("Enter your name: ")

    print("Hello", name)


# Uncomment to test
# user_greeting()


# ============================================================
# MINI PROJECT 1 — CALCULATOR
# ============================================================

def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

    else:
        return "Invalid operation"


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))


# ============================================================
# MINI PROJECT 2 — STUDENT MARKS
# ============================================================

def calculate_average(marks):

    total = 0

    for mark in marks:
        total = total + mark

    return total / len(marks)


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Average:", average)


# ============================================================
# DAY 5 CHALLENGES
# ============================================================

# Challenge 1
# Create a function called subtract(a, b)
# that returns a - b.


# Challenge 2
# Create a function called is_positive(number)
# that returns True if the number is positive.


# Challenge 3
# Create a function called maximum(a, b, c)
# that returns the largest number.


# Challenge 4
# Create a function called count_vowels(word)
# that counts vowels in a word.


# Challenge 5
# Create a function called reverse_word(word)
# that returns the word backwards.


# Challenge 6
# Create a function called calculate_percentage(obtained, total)
# that returns the percentage.


# Challenge 7
# Create a function called factorial(number)
# that calculates factorial.


# Challenge 8
# Create a function called password_check(password)
# that returns True if the password is correct.


# ============================================================
# DAY 5 GOAL
# ============================================================

# By the end of Day 5, you should understand:
#
# def
# parameters
# arguments
# return
# default parameters
# if/else inside functions
# loops inside functions
# lists + functions
# local variables
#
# MOST IMPORTANT:
# Don't just copy the code.
# Change numbers, names and conditions.
# Break the code intentionally and fix it.
