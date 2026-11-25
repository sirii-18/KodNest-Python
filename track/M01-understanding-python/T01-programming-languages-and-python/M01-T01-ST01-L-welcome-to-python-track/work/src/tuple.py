# Tuples -> (), ordered, immutable

nums = (1, 2, 3, 4)
print(nums, type(nums))

# nums[0] = 10      # immutable: TypeError

# index          0      1    2     3
stu_info = ("Nandhu", 22, 8.9, True)
print(stu_info)
print(stu_info[1])
print(stu_info[0:2])
print(stu_info[-2])

# Single element: without trailing comma it is treated as str
name = ("Nandhu")
print(name, type(name))  # <class 'str'>

# Single element tuple requires comma outside quotes
name = ("Nandhu",)
print(name, type(name))  # <class 'tuple'>

name = ("Nandhu",) * 3
print(name, type(name))  # ('Nandhu', 'Nandhu', 'Nandhu') <class 'tuple'>

# Tuple constructor
rgb = tuple("red")
print(rgb, type(rgb))

lst = [1, 2, 3]
print(lst, type(lst))
res = tuple(lst)
print(res)

fruits = ("apple", "bannana")
# fruits.append("mango")  # Tuples do not support modification
# fruits.insert(1, "grape")
# fruits.pop()
# fruits.remove("apple")
# fruits.clear()
print(fruits, type(fruits))
del fruits

# Adding and removing elements via list conversion
x = (1, 2, 3)
y = list(x)
y.append(4)
x = tuple(y)
print(x)

# Adding two tuples (concatenation)
x = (1, 2, 3)
y = (11, 12, 13)
x = x + y
print(x)

# Looping
z = (10, 11, 12, 10)
for i in range(len(z)):
    print(z[i])

# Methods in tuple: count, index
print(z.count(10))
print(z.index(10))
print(z.index(10, 2))

# Unpacking of tuples
emp = ("Nandhida", 22, "Developer")
(name, age, role) = emp
print(name)
print(age)
print(role)

# Packing of tuples
name = "Nandhu"
age = 22
role = "Engineer"
emp = (name, age, role)
print(emp)

# Extended unpacking (*)
s = (2, 4, 6, 8, 10)
(a, *b) = s
print(a)
print(b)

s = (2, 4, 6, 8, 10)
(a, *b, c) = s
print(a)
print(b)
print(c)

# Built-in functions with tuples
t = (10, 20, 30, 40, 50)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(any(t))
print(all(t))
print(10 in t)

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
print(t1 * 2)

del t

# Reversing a tuple
r = (1, 2, 3)
print(tuple(reversed(r)))  # (3, 2, 1)
print(r[::-1])             # (3, 2, 1)