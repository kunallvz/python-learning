first_name = 'kunal'
last_name = 'kumar'
country = 'India'
city = 'Delhi'
age = 20
is_student = True
skills = ['Html','Css','Javascript','python']
#person_info = {
#   'first_name': 'kunal'
#   'last_name':'kumar'
#   'country': 'India' 
#}
# printing the values 
print('first_name:',first_name)
print('last_name:',last_name)
print('country:',country)
print('city:',city)
print('age')
print('skills')
print('student:',is_student) 
#print('person_info:',person_info)
#-------------------------------------------------------------
letter = "A"
print('letter')
print(len(letter))
greeting = 'hello, world!'
print("greeting")
print(len(greeting))
#----------------------------------------------------------- 
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#---------------------------------------------------------- 
#slicing
language = input("what word ")
first_3 = language[0:3]
last_3 = language[8:11]
print(first_3)
print(last_3)
#-------------------------------------------------------- 
word = input("word wt is ")
p = word[0:3:2]
print(p)
#-------------------------------------------------------- 
radius = 10
pi = 3.14
area = pi
result = "the area of circle with {} is {}".format(str(radius),str(area))
print(result)
#----------------------------------------------------------- 
num = '10'
print(num.isdecimal())
num = "10.5"
print(num.isdecimal())

