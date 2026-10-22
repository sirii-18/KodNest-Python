# Add 2 numbers
def add():
    a=5
    b=6
    print(a+b)
    
add()

# Square 2 numbers
def Square():
    a=5
    b=6
    print(a*a,b*b)
    
Square()

# Find the largest number in a list
def largest():
    a =10
    b =20
    c =30
    if a>b and a>c:
        print("a is largest")
    elif b>a and b>c:
        print("b is largest")
    else:
        print("c is largest")
        
largest()

# Check if a number is even or odd
def even_or_odd():
    a = 10
    if a%2 ==0:
        print("Even")
    else:
        print("Odd")
        
even_or_odd()

# Greet with name
def greet():
    name = "John"
    print(f"Hello, {name}")
    
greet()

# No arguments, no return
def sqaure():
    a = 10
    print(a*a)

# No arguments, returns a value
def sqaure():
    a = 10
    return a*a
print(sqaure())

# Arguments, no return
def square(a):
    print(a*a)
square(10)

# Arguments, return a value
def sqaure(a):
    return a*a
res = sqaure(10)
print(res)