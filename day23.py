"""Day 23: practice basic list operations."""

numbers = [3, 1, 4, 1, 5]
print("Original:", numbers)
print("Sorted:", sorted(numbers))
print("Total:", sum(numbers))
#--------------------------------- 
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")
#---------------------------------T
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    #---------T
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
#--------------------------------------- 
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
#---------------------------- 
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")
#---------------------------------- 
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#---------------------------- 
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
#----------------------------- 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")
#--------------------------------+ 
# 5. Find the largest of three numbers
a = 15
b = 25
c = 10

largest = max(a, b, c)
print("Largest number:", largest)

