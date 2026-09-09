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
#---------------------------------------------------- 
# clear
fruits = ['Banana','Apple','orange','Mango']
fruits.clear()
print(fruits)
#---------------------------------------------------- 
#join
pos_num = [1,2,3,4,5]
zero = [0]
nev_num = [-5,-4, -3, -2, -1]
integers = nev_num + zero + pos_num
print(integers)
#--------------------------------+----------------\
# join with extend 
num1 = [0,1,2,3]
num2 = [4,5,6,7]
num1.extend(num2)
print("Numbers:", num1)
#--------------------------------------------------f 
#count 
fruits = ['Banana','Apple','orange','Mango']
fruits.append('orange')
print(fruits)
print(fruits.count('orange'))
#-----------------------------------------            
fruits = ['Banana', 'Apple', 'orange', 'Mango', 'Strawberry']
fruits.reverse()
print(fruits.reverse())
#-------------------------------------------        n 
#sort 
fruits = ['Banana', 'Apple', 'orange', 'Mango', 'Strawberry']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

