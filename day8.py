hollow_list = list()
print(len(hollow_list))
# list of fruits 
fruits = ['Banana','Apple','orange','Mango']
fruits.append('Strawberry')
print("fruits:",fruits)
# using append 
fruits.append('Dragon fruit')
print(fruits)
#------------------------------------------- 
#insert
fruits = ['Banana','Apple','orange','Mango']
fruits.insert(2,'lime')
print(fruits)
#-------------------------------------------- 
# remove 
#fruits = ['Banana','Apple','orange','Mango']
#fruits.remove()
#print(fruits)

#fruits.remove(0)
#print(fruits)
#del --------------------------------------------- 
fruits = ['Banana','Apple','orange','Mango']
del fruits[1]
print(fruits)
del fruits[2]
print(fruits)# error expected 

