#Day 28  python learning 
# streak day 28 
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


car1 = Car("BMW", "Black")
car1.show() 
#--------------------------- 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")


student1 = Student("Kunal", 75)
student1.result()
#-------------------------------- 
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New balance:", self.balance)


account1 = BankAccount("Kunal", 5000)
account1.deposit(2000)
#------------------------------------ 
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


phone1 = Mobile("Samsung", 25000)
phone2 = Mobile("Apple", 50000)

phone1.details()
phone2.details()
