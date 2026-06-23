# Easy:
# Add
def add(a, b):
    return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(add(num1, num2))

# Multiply
def add(a, b):
    return a*b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(add(num1, num2))

# Temperature converter
def celcius_to_farenheit(temp):
    return temp*9/5 + 32

temperature = float(input("Enter celcius temperature: "))
print(f"{temperature} celcius equal: {celcius_to_farenheit(temperature)}")

# Medium:
# 4. GPA calculator
def gpa_calc(n):
    if (n >= 80) and (n <= 100):
        return "A+"
    elif n >= 70 and n < 80:
        return "A"
    elif n >= 60 and n < 70:
        return "A-"
    elif n >= 50 and n < 60:
        return "B"
    elif n >= 40 and n < 50:
        return "B-"
    elif n >= 33 and n < 40:
        return "C"
    else:
        return "Fail"
    
number = int(input("Enter your marks: "))
print(f"Your marks: {number} and GPA: {gpa_calc(number)}")

# 5. Tax system
def vehicle_tax(cc):
    if cc > 0 and cc <= 1500:
        return 25000
    elif cc > 1500 and cc <= 2000:
        return 50000
    elif cc > 2000 and cc <= 2500:
        return 75000
    else:
        return 100000
    
cc = int(input("Enter vehicle CC: "))
print(f"Your engine capacity {cc} CC and your tax is Approximately BDT {vehicle_tax(cc):,} per year.")

# 6. Password checker
def is_pass(p = ""):
    if p == "1234":
        return True
    else:
        return False
    
while not is_pass():
    password = (input("Enter your password: "))

    if is_pass(password):
        print("Log in successfully.")
        break
    else:
        print("Your entered wrong password.")