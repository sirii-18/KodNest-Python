def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
def add(a,b,c,d):
    print(a+b+c+d)

#add(10,20)
#add(10,20,30)
add(10,20,30,40) #python does not support function overloading (only last function will be called)

# Default values
def add(a,b=0,c=0):
    print(a+b+c)

add(1)
add(1,2)
add(1,2,3)

# *args -0 ... n arguments can be passed --> tuple
def add(*a):
    print(sum(a))

add(10,20)
add(10,20,30)
add(10) 
add()

# **kwargs -0 ... n argumnents can be passed --> dict
def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')} ", end="")
    print(f"Age is {kwargs.get('age')} ", end="")
    print(f"Course is {kwargs.get('course')}")

stu_info(name="John",age=21,course="Python")
    
