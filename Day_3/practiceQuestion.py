# Easy:
# Print 1–100
for i in range (1, 101):
    print(i, end=' ')

# Sum numbers
sum = 0
lastNum = int(input("\nEnter last number: "))
for i in range(1, lastNum+1):
    sum += i
print(f"Sum from 1 to {lastNum} is: {sum}")

# Multiplication table
n = int(input("Enter a nummber for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Medium:
# 4. Prime checker
n = int(input("Enter a nummber to check prime or not: "))
is_prime = True
for i in range(2, n):
    if n%i == 0:
        is_prime = False
        break
    
if is_prime:
    print("Prime")
else:
    print("Not prime")

# 5. Factorial
n = int(input("Enter a nummber to calculate factorial: "))
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"Factorial of {n} is: {fact}")

# 6. Reverse number
lastNum = int(input("Enter a number: "))
ans = 0
while lastNum > 0:
    rem = lastNum % 10
    ans = ans*10 + rem
    lastNum //= 10
print(ans)

# Challenge:
# 7. Build ATM PIN attempts system
while True:
    pin = input("Enter PIN: ")
    if int(pin) == 1234:
        print("Accepted..")
        break
        