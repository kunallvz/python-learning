"""Day 27: practice dictionary lookup and updates."""

student = {
    "name": "Kunal",
    "age": 20,
    "course": "Python learning",
}

student["city"] = "New Delhi"
student["age"] = 21

print("Student profile:", student)
print("Name:", student["name"])
print("Course:", student["course"])
#------------------------------ 
# 2. Add and update items in a dictionary
student = {
    "name": "Rahul",
    "age": 15
}

student["class"] = 10
student["age"] = 16

print(student) 
#---------------------- 
# 3. Access values from a dictionary
student = {
    "name": "Rahul",
    "age": 15,
    "city": "Delhi"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"]) 
#------------------------------- 
# 1. Create and display a dictionary
student = {
    "name": "Rahul",
    "age": 15,
    "class": 10
}

print(student)
#------------------------------------- 
# 4. Delete an item from a dictionary
student = {
    "name": "Aman",
    "age": 16,
    "class": 10
}

del student["age"]

print(student)
#---------------------------------- 
# 5. Check if a key exists in a dictionary
student = {
    "name": "Aman",
    "age": 16,
    "class": 10
}

if "name" in student:
    print("Name is present in the dictionary")
else:
    print("Name is not present") 
