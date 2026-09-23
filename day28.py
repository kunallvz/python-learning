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

