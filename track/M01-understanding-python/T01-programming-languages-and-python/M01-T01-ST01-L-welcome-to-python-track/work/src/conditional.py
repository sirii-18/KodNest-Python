# part 1 -if,If-else,if-elif-else

num1 = int(input("Enter first number: "))
if num1>0:
    positive = None
    print('positive')
else:
    print('negative')

age = int(input("Enter the Age"))
if age >= 18:
    print("Eligible")
else :
    print("Not Eligible")

temp = int(input("Enter the Temperature"))
if temp > 30:
    print("Hot Day")

No_classes_attended = int(input("Enter number of the classes attended"))
if No_classes_attended >= 75:
    print("The student has attended at least 75% of the classes")
else:
    print("The student has not attended at least 75% of the classes")

number = int(input("Enter a Number"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

Age = int(input("Enter the age"))
if age >=18 and age <= 60:
    print("Adult")
else:
    print("Not adult")

# Leap year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print ("Leap")
    else:
        print("Not a leap")

num1= int(input("Enter the number 1"))
num2= int(input("Enter the number 2"))
if num1>num2:
    print("Number 1 is Greater")
else:
    print("Number 2 is greater")

marks = int(input("Enter the Marks"))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
else:
    print("Fail")

Electricity_usage = int(input("Enter the Electricity usage in units"))
if Electricity_usage > 500:
    print("High usage")
elif Electricity_usage >= 301 and Electricity_usage <= 500:
    print("Medium usage")
elif Electricity_usage >= 101 and Electricity_usage <= 300:
    print("Low usage")
else:
    print("Very low usage")

Marks = int(input("Enter the Marks"))
family_income = int(input("Enter the family income"))
if Marks >= 85 and family_income < 300000:
    print("Eligible for scholarship")
else:
    print("Not Eligible for scholarship")

user_name = str(input("Enter the username"))
user_password = str(input("Enter the password"))
if user_name == user_password:
    print("Login successful")
else:
    print("Invalid credentials")

# Display weekday using numbers (1-7)
num = int(input("Enter the number"))
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid number")

# Display season based on the month number (1-12)
# Dec,Jan,Feb -> Winter
# Mar,Apr,May -> Spring
# Jun,Jul,Aug -> Summer
# Sep,Oct,Nov -> Autumn
num = int(input("Enter the month number"))
if num == 12 or num == 1 or num == 2:
    print("Winter")
elif num == 3 or num == 4 or num == 5:
    print("Spring")
elif num == 6 or num == 7 or num == 8:
    print("Summer")
elif num == 9 or num == 10 or num == 11:
    print("Autumn")
else:
    print("Invalid number")

# for loop
for i in range (1,11): 
    print(i) # output from 1 to 10

num = int(input("Enter the number: ")) # Multiplication table of given number
for i in range(1,11):
    print(num*i) # output of table of given number  

# while loop
# print numbers from 10 to 1
def countdown():
    num = 10
    while num > 0:
        print(num)
        num -= 1

countdown()


# factorial of a number
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)  

# Break Statements
# print numbers from 1 to 20 but stop at 15
for i in range(1,20):
    if i==15:
        break
    print(i) #output 

# search for a number in a list using break
for i in range(1,20):
    if i==15:
        break
    print(i) #output 

# Continue Statements
# print numbers from 1 to 50 but skip numbers divisible by 5
for i in range(1,50):
    if i%5==0:
        continue
    print(i) #output except 5 10 15 20 25 30 35 40 45 50

# print odd numbers from 1 to 50
for i in range(1,50):
    if i%2==0:
        continue
    print(i)







