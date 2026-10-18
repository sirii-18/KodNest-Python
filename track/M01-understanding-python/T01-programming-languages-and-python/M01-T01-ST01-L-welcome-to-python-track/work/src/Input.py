name = input("Enter the name:")
print(f"the name is {name}")

age = input("Enter the age:")
print(f"the age is {age}")

# To add 2 nums
first = input("Enter first number:")
second = input("Enter second number:")
print(f"The sum of {first} and {second} is {first+second}")
#input() default data type is str

# To add 2 nums
first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
print(f"The sum of {first} and {second} is {first+second}")

# To add 2 nums
first = float(input("Enter first number:"))
second = int(input("Enter second number:"))
print(f"The sum of {first} and {second} is {first+second}")

#taking a boolean input from the user
user_response = input("Do you like ice cream? (yes/no):").lower()
is_ice_cream_lover = user_response == "yes"
print ("Do you like ice cream?",is_ice_cream_lover)