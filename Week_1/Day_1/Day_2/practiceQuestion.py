# Easy:
# Odd / Even
n = int(input("Enter a number: ")) 
if n % 2 == 0:
    print("Even number")
else:
    print("Odd nmber")

# Largest of 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")
else:
    if b > c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

# Grade calculator
n = int(int("Enter your score: "))
if (n >= 80) and (n <= 100):
    print("A+")
elif n >= 70 and n < 80:
    print("A")
elif n >= 60 and n < 70:
    print("A-")
elif n >= 50 and n < 60:
    print("B")
elif n >= 40 and n < 50:
    print("B-")
elif n >= 33 and n < 40:
    print("C")
else:
    print("Fail")

# Positive/Negative
n = int(int("Enter your score: "))
if n < 0:
    print("number is Negetive")
else:
    print("Number is prositive")

# Medium:
# 5. BMI calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meter: "))

bmi = weight/(height*height)
print(f"Your BMI: {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Healthy Weight")
elif bmi >= 25.5 and bmi < 30.0:
    print("Overweight")
else:
    print("Obese")

# 6. Login validation
username = input("Enter username: ")
password = input("Enter password: ")

if username == 'maiyan' and password == '1234':
    print("Log in successfully")
else:
    print("Log in failed")


