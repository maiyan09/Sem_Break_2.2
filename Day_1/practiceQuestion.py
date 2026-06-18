# Practice Questions
# Print your name
name = "Samiur Rahman Maiyan"
print(name)

# Take name input and greet
myName = input("Enter Your Name: ")
print(f"Hello, {myName}. Welcome to Python.")

# Convert Celsius → Fahrenheit
temp = float(input("Enter temperature in celcius: "))
print(f"Temperature in Fahrenheit is {(temp*9/5) + 32} degree")

# Calculate age
year = int(input("Enter your birth year: "))
print(f"Your age is: {2026-year}")

# Area of rectangle
length = float(input("Enter lenght: "))
width = float(input("Enter width: "))
print("Area of rectangle: ", length*width)

# Swap two numbers
a = 20
b = 10
print(f"Befor swap: a is {a} and b is {b}")
a, b = b, a
print(f"After swap: a is {a} and b is {b}")

# Convert minutes → hours
minute = int(input("Enter minute: "))
print(f"{minute} minute equal {minute/60} hour")
