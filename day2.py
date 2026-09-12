# Day 2 - Python practice: Variables and Types
# Streak day 2

# Variables
message = "Hello again, from kunal!"
count = 20
pi_approx = 3.14
is_learning = True

print(message)
print("count:", count)
print("pi_approx:", pi_approx)
print("is_learning:", is_learning)

# Types and type checking
print(type(message))   # <class 'str'>
print(type(count))     # <class 'int'>
print(type(pi_approx)) # <class 'float'>
print(type(is_learning))

# Simple arithmetic
sum_result = count + int(pi_approx)
print("sum_result:", sum_result)

# Example of user input (commented out to avoid blocking runs)
# name = input("What's your name? ")
# print(f"Nice to meet you, {name}!")

# Exercises (try these):
# 1) Create two variables a and b, assign numbers, and print their product. 
a = 5
b = 10
print("Sum of a and b:", a + b)
print("Product of a and b:", a * b)

# 2) Convert a float to an int and observe the result.
float_num = 3.99
int_num = int(float_num)
print(f"Float {float_num} converted to int: {int_num}")

# 3) Create a boolean variable and use it in an if statement to print a message.
is_active = True
if is_active:
    print("User is active!")
else:
    print("User is not active")
