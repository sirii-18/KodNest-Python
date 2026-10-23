name = "Sirisha"
age = 21
print(name)
print(id(name))
print(type(name))

print("Hello Python", end=" - ")
print("Thank you Python")

print("Hello Python \nThank you Python")

# My name is Sirisha and age is 21
print("My name is " + name + " and age is " + str(age))

#String Formating (f strings)
print(f"My name is {name} and age is {age}")

# Single - line comments

""" Multi - line comments
Hi
Hello 
Thank you
"""

a = 10
b = 20
c = 30
# a,b,c=10,20,30
# Addition 
a=b=c=10
print(a+b+c)

a, b, c = "Sirisha", "Yash", "RCB"
print(b)
print(a + b + c)

x,y,z = 30,4,8
print(x + z) # =38
print(a + str(z)) # = "Sirisha" + "8" = "Sirisha8"  
print(b + c) # YashRCB
print(a , x) # Sirisha 30

# local and global variables
c = 30
def add():
    a = 10 #local variable
    b = 20 #local variable
    print(a+b) # local variables can be accessed only inside the function
    print(c) # global variable can be accessed only outside the function
add()
print(c) # global variable can be accessed only outside the function

x = 100 #global variable
def display():
    x = 50 #local variable
    print("Local x:",x) #local variable is given the first priority
display()
print("Global x:",globals()) #global variables can be accessed only outside the function

x = 10

def display():
    print(globals()['x'])  # 10 (global)
    x = 20                 # local variable
    print(x)               # 20 (local)

display()
x = 30
print(x)                   # 30

# nested function
x = 10
def display():
    x = 20
    def inner_display():
        print(x)  # Python looks for x in:
                  # 1) inner_display's scope → not found
                  # 2) display's scope  → x = 20
                  # 3) global scope   → x = 10
                  # Result: prints 20
    inner_display()
display()

