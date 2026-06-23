# Practice
# Save notes
while True:
    try:
        print("1. Save note")
        print("2. Leave")
        n = int(input("Enter choice: "))
        if n == 1:
            note = input("Write your note: ")
            with open('note.txt', 'a') as file:
                file.write('- ' + note + '\n')
        elif n == 2:
            break
    except ValueError as v:
        print("Error occurs: Enter number 1 or 2")
    
# Read file
with open('note.txt', 'r') as read:
    contents = read.read()
    print(contents)

# Error on divide
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print(f"{numerator}/{denominator} = {result}")
    
except ZeroDivisionError:
    print("Denominator mst be greater than zero..")
    
except ValueError:
    print("Enter number..")

# Login attempts
password = "man09"
attempts = 3

while attempts > 0:
    p = input("Enter password: ")

    if p == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong password.")

if attempts == 0:
    print("Account locked.")