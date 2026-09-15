# ============================================================
# PYTHON DAY 13
# TOPIC: OBJECT-ORIENTED PROGRAMMING BASICS (OOP)
# ============================================================

print("===== DAY 13: OBJECT-ORIENTED PROGRAMMING =====\n")

# ============================================================
# 1. CLASSES AND OBJECTS
# ============================================================

print("--- 1. CLASSES AND OBJECTS ---")

class Car:
    """A simple Car class"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

# Create objects (instances)
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

car1.display_info()
car2.display_info()

print()

# ============================================================
# 2. ATTRIBUTES AND METHODS
# ============================================================

print("--- 2. ATTRIBUTES AND METHODS ---")

class Student:
    """A Student class with attributes and methods"""
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_details(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}")
    
    def calculate_percentage(self):
        total = sum(self.marks)
        percentage = (total / (len(self.marks) * 100)) * 100
        return percentage
    
    def display_result(self):
        percentage = self.calculate_percentage()
        print(f"{self.name}: {percentage:.2f}%")

student1 = Student("Kunal", "S001", [85, 90, 88, 92])
student1.display_details()
student1.display_result()

print()

# ============================================================
# 3. CONSTRUCTOR (__init__)
# ============================================================

print("--- 3. CONSTRUCTOR (__init__) ---")

class Person:
    """Person class with constructor"""
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        print(f"Person object created: {self.name}")
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

person1 = Person("Alice", 25, "alice@example.com")
person1.introduce()

person2 = Person("Bob", 30, "bob@example.com")
person2.introduce()

print()

# ============================================================
# 4. INSTANCE VARIABLES VS CLASS VARIABLES
# ============================================================

print("--- 4. INSTANCE VS CLASS VARIABLES ---")

class BankAccount:
    """Bank Account with class and instance variables"""
    bank_name = "MyBank"  # Class variable (shared by all instances)
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance variable
        self.balance = balance  # Instance variable
    
    def display_info(self):
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

acc1 = BankAccount("Kunal", 5000)
acc2 = BankAccount("Priya", 8000)

acc1.display_info()
print()
acc2.display_info()

print()

# ============================================================
# 5. METHODS
# ============================================================

print("--- 5. METHODS ---")

class Calculator:
    """Calculator class with various methods"""
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        self.result = x + y
        return self.result
    
    def subtract(self, x, y):
        self.result = x - y
        return self.result
    
    def multiply(self, x, y):
        self.result = x * y
        return self.result
    
    def divide(self, x, y):
        if y == 0:
            print("Error: Division by zero!")
            return None
        self.result = x / y
        return self.result
    
    def get_result(self):
        return self.result

calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"20 / 4 = {calc.divide(20, 4)}")
print(f"Last result: {calc.get_result()}")

print()

# ============================================================
# 6. SPECIAL METHODS (__str__, __repr__)
# ============================================================

print("--- 6. SPECIAL METHODS ---")

class Book:
    """Book class with special methods"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book1 = Book("Python Basics", "John Doe", 350)
print(f"str(): {str(book1)}")
print(f"repr(): {repr(book1)}")
print(f"print(): {book1}")

print()

# ============================================================
# 7. SELF PARAMETER
# ============================================================

print("--- 7. SELF PARAMETER ---")

class Rectangle:
    """Rectangle class demonstrating self"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display(self):
        print(f"Width: {self.width}, Height: {self.height}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

rect = Rectangle(5, 10)
rect.display()

print()

# ============================================================
# 8. OBJECT IDENTITY AND EQUALITY
# ============================================================

print("--- 8. OBJECT IDENTITY AND EQUALITY ---")

class Point:
    """Point class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = p1

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 is p2: {p1 is p2}")
print(f"p1 is p3: {p1 is p3}")

print()

# ============================================================
# 9. ISINSTANCE AND TYPE
# ============================================================

print("--- 9. ISINSTANCE AND TYPE ---")

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(f"type(dog): {type(dog)}")
print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, str): {isinstance(dog, str)}")

print()

# ============================================================
# 10. PRACTICAL EXAMPLE: BANK ACCOUNT SYSTEM
# ============================================================

print("--- 10. PRACTICAL EXAMPLE: BANK ACCOUNT ---")

class BankAccountAdvanced:
    """Advanced Bank Account with deposit/withdraw"""
    def __init__(self, holder, initial_balance=0):
        self.holder = holder
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -${amount}")
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient balance!")
    
    def display_balance(self):
        print(f"Account Holder: {self.holder}")
        print(f"Balance: ${self.balance}")
    
    def display_history(self):
        print(f"\nTransaction History for {self.holder}:")
        for transaction in self.transactions:
            print(f"  {transaction}")

account = BankAccountAdvanced("Kunal", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(300)
account.display_balance()
account.display_history()

print()

# ============================================================
# DAY 13 CHALLENGES
# ============================================================

# Challenge 1: Create a Student class with marks calculation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)


student = Student("Kunal", [80, 75, 90, 85, 70])

print("Name:", student.name)
print("Total:", student.total_marks())
print("Average:", student.average_marks())
# Challenge 2: Create a Movie class with __str__ method
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"{self.title} directed by {self.director} ({self.year})"


movie = Movie("Interstellar", "Christopher Nolan", 2014)

print(movie)
# Challenge 3: Create a Library class with add/remove books
# Challenge 4: Create a Temperature class with C to F conversion
# Challenge 5: Create a Circle class with area and circumference
# Challenge 6: Create a Person class with age validation
# Challenge 7: Create an Employee class with salary calculation
# Challenge 8: Create a To-Do class with add/remove tasks

print("✓ Day 13 completed!")
