"""Day 24: practice a simple dictionary lookup."""

student = {"name": "Alex", "score": 92}
print(f"{student['name']} scored {student['score']}.")
#+---------------- 
# Dictionary lookup

student = {
    "name": "Rahul",
    "age": 15,
    "class": 10,
    "city": "Delhi"
}

key = input("Enter the key to look up: ")

if key in student:
    print("Value:", student[key])
else:
    print("Key not found") 
#---------------------- 
# Phone book lookup

phone_book = {
    "Rahul": "9876543210",
    "Aman": "9876501234",
    "Priya": "9876512345"
}

name = input("Enter name: ")

if name in phone_book:
    print("Phone number:", phone_book[name])
else:
    print("Name not found") 
#------------ 
print("dictionary") 
