#Day 6 cs50 python courrse lecture 0 
#streak Day 6 
# Divison 
x = float(input("what is x? "))
y = float(input("what is y? "))

z = round(x/y,2)
print(z)
# def function 
#def main():
 #   name = input("what your name ")
  #  hello(name)
#def hello(to = "world"):
#          print("hello,",to)
#main()
#=======================================================
# square root number
def main2():
    x = int(input("x "))
    def square(n):
        return n**2
    print("x squared is",square(x))
main2()
#=======================================================
# cube root 
def main3():
    y = int(input("y "))
    def cube(n):
        return pow(n,3)
    print("y is cube to ",cube(y))
main3()

