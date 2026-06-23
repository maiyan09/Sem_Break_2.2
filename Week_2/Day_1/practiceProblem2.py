# Practice
import random
from datetime import datetime
# Import own module
import mymodule
name = input("Enter your name: ")
mymodule.greeting(name)

# Random password generator
def passwordGenerator():
    char = ''
    for i in range(0, 3): #Generate 3 capital letter
        char += chr(random.randint(65, 90))
    for i in range(0, 3): #Generate 3 small letter
        char += chr(random.randint(97, 122))
    for i in range(0, 3): #Generate 3 symbol (@!$) letter
        char += chr(random.randint(33, 47))
    num = random.randint(100, 999)
    char += str(num)
    return char

attepts = 4
for i in range(0, 5):
    print("1. Generate password.")
    print("2. Stop.")
    n = int(input("Enter choice: "))
    
    if n == 1:
        print(f"You have {attepts} attepts left.")
        print(f"\nSuggested Password: {passwordGenerator()}\n")
        attepts -= 1
    elif n == 2:
        break

# Dice simulator
def roll_dice():
    return random.randint(1, 6)

while True:
    print(f"You rolled: {roll_dice()}")

    choice = input("Roll again? (y/n): ").lower()

    if choice != 'y':
        break
    
# Age calculator using datetime
daate = int(input("Enter birth date: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

date = datetime(year, month, daate)

print("\nYou born on: ", date.strftime("%A"))

years = datetime.now().year - year
months = datetime.now().month - month

if months < 0:
    months += 12
    year -= 1
    
print(f"You lived: {years} years and {months} months\n")
