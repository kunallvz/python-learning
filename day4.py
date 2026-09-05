#Daily python practice and learning 
#streak day 4
#print("day 4 find the topic")
#def hello(name):
#print("Hello,",name)
# x=10 
# y=20
 #return x+y 
 #hello("Kunal")
# ============================================================
# PYTHON FUNCTIONS - BEGINNER PRACTICE SHEET
# ============================================================


# ------------------------------------------------------------
# 1. SIMPLE FUNCTION
# ------------------------------------------------------------

def say_hello():
    # This function simply prints a message
    print("Hello, Kunal!")


# Calling the function
say_hello()


# ------------------------------------------------------------
# 2. FUNCTION WITH A PARAMETER
# ------------------------------------------------------------

def greet(name):
    # 'name' is a parameter
    print("Hello,", name)


# Passing a value to the function
greet("Kunal")
greet("Rahul")


# ------------------------------------------------------------
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ------------------------------------------------------------

def add_numbers(a, b):
    # Add two numbers
    result = a + b

    # Display the result
    print("Answer:", result)


add_numbers(10, 20)
add_numbers(50, 30)


# ------------------------------------------------------------
# 4. FUNCTION THAT RETURNS A VALUE
# ------------------------------------------------------------

def add(a, b):
    # Instead of printing the answer,
    # return sends the answer back to where
    # the function was called.
    return a + b


answer = add(10, 20)

print("The answer is:", answer)


# ------------------------------------------------------------
# 5. RETURN MULTIPLICATION
# ------------------------------------------------------------

def multiply(a, b):
    return a * b


result = multiply(5, 6)

print("Multiplication:", result)


# ------------------------------------------------------------
# 6. CHECK EVEN OR ODD
# ------------------------------------------------------------

def check_even(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even(10))
print(check_even(7))


# ------------------------------------------------------------
# 7. FIND THE LARGER NUMBER
# ------------------------------------------------------------

def larger_number(a, b):

    if a > b:
        return a
    else:
        return b


print("Larger:", larger_number(50, 30))


# ------------------------------------------------------------
# 8. FUNCTION WITH DEFAULT VALUE
# ------------------------------------------------------------

def welcome(name="User"):
    # If no name is given,
    # Python will use "User"
    print("Welcome", name)


welcome("Kunal")
welcome()


# ------------------------------------------------------------
# 9. FUNCTION USING A LOOP
# ------------------------------------------------------------

def print_numbers(n):

    for i in range(1, n + 1):
        print(i)


print_numbers(5)


# ------------------------------------------------------------
# 10. CALCULATE SQUARE
# ------------------------------------------------------------

def square(number):

    return number * number


print("Square:", square(8))


# ------------------------------------------------------------
# 11. CALCULATE POWER
# ------------------------------------------------------------

def power(number, exponent):

    return number ** exponent


print("Power:", power(2, 5))


# ------------------------------------------------------------
# 12. CALCULATE AVERAGE
# ------------------------------------------------------------

def average(a, b, c):

    total = a + b + c

    return total / 3


print("Average:", average(10, 20, 30))


# ------------------------------------------------------------
# 13. FUNCTION WITH USER INPUT
# ------------------------------------------------------------

def introduce():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("My name is", name)
    print("I am", age, "years old")


# Uncomment this when you want to test it
# introduce()


# ------------------------------------------------------------
# 14. FUNCTION TO CHECK PASSWORD
# ------------------------------------------------------------

def check_password(password):

    if password == "python123":
        return "Correct password"
    else:
        return "Wrong password"


print(check_password("python123"))
print(check_password("hello"))


# ------------------------------------------------------------
# 15. FUNCTION TO FIND FACTORIAL
# ------------------------------------------------------------

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


print("Factorial:", factorial(5))


# ------------------------------------------------------------
# 16. FUNCTION TO CHECK PRIME NUMBER
# ------------------------------------------------------------

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))


# ------------------------------------------------------------
# 17. FUNCTION USING A LIST
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
# 18. FUNCTION TO COUNT ITEMS
# ------------------------------------------------------------

def count_items(items):

    count = 0

    for item in items:
        count = count + 1

    return count


fruits = ["apple", "banana", "mango"]

print("Number of fruits:", count_items(fruits))


# ------------------------------------------------------------
# 19. FUNCTION TO CONVERT CELSIUS TO FAHRENHEIT
# ------------------------------------------------------------

def celsius_to_fahrenheit(celsius):

    return (celsius * 9 / 5) + 32


print(celsius_to_fahrenheit(25))


# ------------------------------------------------------------
# 20. MINI CALCULATOR USING FUNCTIONS
# ------------------------------------------------------------

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
# FUNCTION PRACTICE CHALLENGES
# ============================================================

# Try solving these WITHOUT looking at the answers online.


# Challenge 1:
# Create a function called subtract(a, b)
# that returns a - b.


# Challenge 2:
# Create a function called is_positive(number)
# that returns True if the number is positive
# and False otherwise.


# Challenge 3:
# Create a function called maximum(a, b, c)
# that returns the largest of three numbers.


# Challenge 4:
# Create a function called count_vowels(word)
# that counts how many vowels are in a word.


# Challenge 5:
# Create a function called reverse_word(word)
# that returns the word backwards.


# Challenge 6:
# Create a function called calculate_percentage(total, obtained)
# that returns the percentage.


# Challenge 7:
# Create a function called multiplication_table(number)
# that prints the multiplication table from 1 to 10.


# Challenge 8:
# Create a function called sum_list(numbers)
# that returns the sum of all numbers in a list.
