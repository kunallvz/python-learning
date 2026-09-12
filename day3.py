# Day 3 - Python practice: Control Flow
# Streak day 3

# If / elif / else
x = 7
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")

# For loop with range
for i in range(5):
    print("for i:", i)

# Looping over a list with enumerate
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(idx, fruit)

# While loop
counter = 0
while counter < 3:
    print("while counter:", counter)
    counter += 1

# break and continue example
for n in range(1, 10):
    if n == 7:
        print("found 7, breaking")
        break
    if n % 2 == 0:
        continue
    print("odd number before break:", n)

# Exercises:
# 1) Write a loop that computes the sum of numbers from 1 to 100.
total_sum = 0
for i in range(1,101):
    total_sum += i
    print("the numver is :",total_sum)
# 2) Use if/elif/else to print whether a number is negative, zero, or positive.
number = int(input("nunber if choice")) 
if number > 0:
    print("the number is positive")
elif number == 0:
    print("the number is zero")
else:
    print("the number is negative")
# 3) Write a function that checks whether a given number is prime and use it to find primes between 10 and 30.
#def is_prime(n):
#   if n <= 1:
#       return False
#for i in range(2, int(n**0.5)+1):
#    if n % i == 0:
#        return False
#return True
#print("the numbers btw 10 and 30: ")
#for num in range(10, 31):
#    if is_prime(num):
#        print(num, end=" ")
