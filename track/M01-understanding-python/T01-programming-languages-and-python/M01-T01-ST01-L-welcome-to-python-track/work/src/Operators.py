# Arithmetric operators
a=10
b=20
print(a+b) # + -> addition
print(a-b) # - -> subtraction
print(a*b) # * -> multiplication
print(a/b) # / -> division
print(a%b) # % -> modulo
print(a**b) # ** -> exponentiation

# Comparison operators (T/F)
a=10
b=20
print(a==b)  # == -> True if both are equal
print(a!=b)  # != -> True if both are not equal
print(a>b)   # > -> True if a is greater than b
print(a<b)   # < -> True if a is less than b
print(a>=b)  # >= -> True if a is greater than or equal to b
print(a<=b)  # <= -> True if a is less than or equal to b

# Assignment operators
a = 10
print(a)
a += 10  # a = a+10
print(a)
a -= 10  # a = a-10
print(a)
a *= 10  # a = a*10
print(a)
a /= 10  # a = a/10
print(a)
a %= 10  # a = a%10
print(a)
a **= 10 # a = a**10
print(a)
a //= 10 # a = a//10
print(a)

# Logical Operators
a = 10
b = 20
print(a>10 and b>10) #AND -> (F and T) = F
print(a>10 or b>10) #OR -> (F or T) = T
print(not(a>10 and b>10)) #NOT -> (T) = F   

# Identity Operators
a = True
print(a is True)
print(a is not True)

a = 10
b = 10
print(a is b) # is -> checks if the values are same
print(a is not b) # is not -> checks if the values are not same
print(a==b) # == -> checks if the values are equal

# Membership Operators
a = [ 1,2,3,4,5]
print(a in range(1,6)) # true
print(a not in range(1,6)) # false
print(1 in a) # true
print(6 in a) # false
print(6 not in a) # true

# Bitwise Operators
a = 2
b = 3
print(a & b) # -> AND
print(a | b) # -> OR
print(a ^ b) # -> XOR
a = 5
print(~a) # -> NOT
print(a << b) # -> Left Shift
print(a >> b) # -> Right Shift







