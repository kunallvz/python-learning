# ============================================================
# PYTHON DAY 14
# TOPIC: INHERITANCE, POLYMORPHISM & ENCAPSULATION
# ============================================================

print("===== DAY 14: INHERITANCE & POLYMORPHISM =====\n")

# ============================================================
# 1. INHERITANCE - BASIC CONCEPT
# ============================================================

print("--- 1. INHERITANCE - BASIC CONCEPT ---")

class Animal:
    """Parent class (Base class)"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

class Dog(Animal):
    """Child class (Derived class) inheriting from Animal"""
    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

# Create objects
dog = Dog("Buddy", "Canis familiaris")
dog.display_info()
dog.eat()
dog.sleep()
dog.bark()

print()

# ============================================================
# 2. METHOD OVERRIDING
# ============================================================

print("--- 2. METHOD OVERRIDING ---")

class Vehicle:
    """Parent Vehicle class"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"Starting {self.brand} {self.model}")
    
    def stop(self):
        print(f"Stopping {self.brand} {self.model}")

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def start(self):  # Override parent method
        print(f"Car {self.brand} {self.model} is starting with engine")
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Doors: {self.doors}")

class Bicycle(Vehicle):
    """Bicycle class inheriting from Vehicle"""
    def start(self):  # Override parent method
        print(f"Bicycle {self.brand} {self.model} is ready to ride")

car = Car("Toyota", "Camry", 4)
car.start()
car.display_info()
car.stop()

print()

bike = Bicycle("Hero", "Cycle")
bike.start()
bike.stop()

print()

# ============================================================
# 3. SUPER() FUNCTION
# ============================================================

print("--- 3. SUPER() FUNCTION ---")

class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor called for {name}")
    
    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
        print(f"Child constructor called for {name}, age {age}")
    
    def greet(self):
        super().greet()  # Call parent method
        print(f"I'm {self.age} years old")

child = Child("Kunal", 20)
child.greet()

print()

# ============================================================
# 4. MULTILEVEL INHERITANCE
# ============================================================

print("--- 4. MULTILEVEL INHERITANCE ---")

class LivingBeing:
    """Level 1: Grandparent class"""
    def __init__(self):
        self.alive = True

class Mammal(LivingBeing):
    """Level 2: Parent class"""
    def __init__(self):
        super().__init__()
        self.warm_blooded = True

class Human(Mammal):
    """Level 3: Child class"""
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Alive: {self.alive}")
        print(f"Warm-blooded: {self.warm_blooded}")

human = Human("Alice")
human.display()

print()

# ============================================================
# 5. MULTIPLE INHERITANCE
# ============================================================

print("--- 5. MULTIPLE INHERITANCE ---")

class Flyer:
    """Mixin class for flying ability"""
    def fly(self):
        print(f"{self.name} is flying")

class Swimmer:
    """Mixin class for swimming ability"""
    def swim(self):
        print(f"{self.name} is swimming")

class Duck(Flyer, Swimmer):
    """Duck inherits from both Flyer and Swimmer"""
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        print(f"{self.name} goes: Quack! Quack!")

duck = Duck("Donald")
duck.fly()
duck.swim()
duck.quack()

print()

# ============================================================
# 6. POLYMORPHISM - SAME METHOD, DIFFERENT BEHAVIOR
# ============================================================

print("--- 6. POLYMORPHISM ---")

class Shape:
    """Base class for shapes"""
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")

print()

# ============================================================
# 7. ENCAPSULATION - PUBLIC, PRIVATE, PROTECTED
# ============================================================

print("--- 7. ENCAPSULATION ---")

class BankAccount:
    """Bank Account with encapsulation"""
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance  # Private attribute (name mangling)
        self._account_type = "Savings"  # Protected attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}")
        else:
            print("Invalid amount or insufficient balance!")
    
    def get_balance(self):
        return self.__balance
    
    def display_info(self):
        print(f"Holder: {self.holder}, Balance: ${self.__balance}")

account = BankAccount("Kunal", 1000)
account.deposit(500)
account.withdraw(200)
account.display_info()

# Try to access private attribute (name mangling)
print(f"Private balance (mangled): {account._BankAccount__balance}")

print()

# ============================================================
# 8. ABSTRACT CLASSES
# ============================================================

print("--- 8. ABSTRACT CLASSES ---")

from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract Employee class"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # 20% bonus

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15  # 15% bonus

manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)

manager.display_info()
print(f"Bonus: ${manager.calculate_bonus()}")

print()

developer.display_info()
print(f"Bonus: ${developer.calculate_bonus()}")

print()

# ============================================================
# 9. CLASS METHODS AND STATIC METHODS
# ============================================================

print("--- 9. CLASS METHODS AND STATIC METHODS ---")

class MathUtil:
    pi = 3.14159
    
    @staticmethod
    def add(x, y):
        """Static method - doesn't need instance or class"""
        return x + y
    
    @classmethod
    def get_pi(cls):
        """Class method - receives class as first argument"""
        return cls.pi
    
    def multiply(self, x, y):
        """Instance method"""
        return x * y

# Call static method
print(f"Add (static): {MathUtil.add(5, 3)}")

# Call class method
print(f"Pi (classmethod): {MathUtil.get_pi()}")

# Call instance method
util = MathUtil()
print(f"Multiply (instance): {util.multiply(4, 5)}")

print()

# ============================================================
# 10. PRACTICAL EXAMPLE: SCHOOL MANAGEMENT SYSTEM
# ============================================================

print("--- 10. PRACTICAL EXAMPLE: SCHOOL SYSTEM ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Staff(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, age, employee_id, salary, subject):
        super().__init__(name, age, employee_id, salary)
        self.subject = subject
    
    def display_info(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}, Salary: ${self.salary}")

class Principal(Staff):
    def __init__(self, name, age, employee_id, salary, school_name):
        super().__init__(name, age, employee_id, salary)
        self.school_name = school_name
    
    def display_info(self):
        print(f"Principal: {self.name}, School: {self.school_name}, Salary: ${self.salary}")

teacher = Teacher("Rajesh", 40, "T001", 50000, "Mathematics")
principal = Principal("Dr. Sharma", 55, "P001", 80000, "Green Valley School")

teacher.display_info()
principal.display_info()

print()

# ============================================================
# DAY 14 CHALLENGES
# ============================================================

# Challenge 1: Create Vehicle hierarchy with Car, Bike, Truck
# Challenge 2: Create Shape hierarchy with polymorphic area()
# Challenge 3: Create Animal hierarchy with different sounds
# Challenge 4: Create Employee hierarchy with bonus calculation
# Challenge 5: Use abstract class for payment methods
# Challenge 6: Create a Library system with Book and Member classes
# Challenge 7: Implement encapsulation with private attributes
# Challenge 8: Create a game with polymorphic characters

print("✓ Day 14 completed!")
