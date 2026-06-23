# Python First 7 Days — Learning Notes & Practice

Author: Your Name
Goal: Learn practical Python for AI Automation & Software Development

---

# Introduction

This document contains everything I learned in my first 7 days of Python.

## Basic Theory: What is Python?

Python is a high-level, interpreted programming language that is known for its simple syntax and readability. It is widely used in:

* Web development
* Data analysis
* Automation
* Artificial intelligence
* Machine learning
* Scripting
* Backend development

Python is a great language for beginners because it allows you to focus on problem-solving instead of complicated syntax.

## Why Learn Python?

* Easy to read and write
* Large community and support
* Useful for many fields
* Strong demand in jobs and freelancing
* Excellent for automation and AI-related work

## Goals

* Understand Python fundamentals
* Build problem-solving ability
* Create mini projects
* Prepare for APIs and AI development

Rule:
Learn → Practice → Build → Publish

---

# Setup & Installation

Before starting the first 7 days, make sure Python is installed on your system.

## Check if Python is Installed

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

## Install Python

If Python is not installed, download it from:

* https://www.python.org/downloads/

During installation on Windows, make sure to check:

* Add Python to PATH

## Check pip

`pip` is the package manager for Python.

```bash
pip --version
```

If needed, try:

```bash
python -m pip --version
```

## Create a Virtual Environment

A virtual environment keeps your project dependencies separate.

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

## Install Packages for Future Use

You do not need external packages for Days 1–7, but later you may need them.

Example:

```bash
pip install requests
pip install beautifulsoup4
```

## Run a Python File

```bash
python filename.py
```

If needed:

```bash
python3 filename.py
```

---

# Day 1 — Python Basics

## Basic Theory

Python programs are made of instructions that the computer follows step by step. Before writing logic, you need to understand how to store values, display output, take input from users, and convert data into the correct type.

The most important beginner concepts are:

* Variables: store data
* Data types: define what kind of data you are using
* Input/output: interact with users
* Type conversion: change one data type into another
* f-Strings: format output in a clean way

## Topics

* Variables
* Data Types
* Input / Output
* Type Conversion
* f-Strings

---

## Variables

Variables store information.

Example:

```python
name = "Samiur"
age = 22

print(name)
print(age)
```

Output:

```text
Samiur
22
```

---

## Data Types

Common Python data types include:

* `str` for text
* `int` for whole numbers
* `float` for decimal numbers
* `bool` for true/false values

Example:

```python
name = "Alex"
age = 25
cgpa = 3.88
student = True
```

Types:

```python
print(type(name))
print(type(age))
print(type(cgpa))
```

---

## Input

Input allows the user to enter data into the program.

Example:

```python
name = input("Enter name: ")

print("Hello", name)
```

---

## Type Conversion

Sometimes input comes as text, but you need numbers for calculations. Type conversion helps convert one type into another.

Example:

```python
age = input("Enter your age: ")
age = int(age)

print(age + 1)
```

---

## f-Strings

f-Strings are a simple way to insert variables into text.

Example:

```python
name = "Mayan"
cgpa = 3.70

print(f"{name} has CGPA {cgpa}")
```

---

## Practice

1. Area of rectangle
2. Age calculator
3. Celsius converter

---

## Mini Project

Student Information System

```python
name = input("Enter your name: ")
department = input("Enter your department: ")

print(f"Welcome {name}")
print(f"Department: {department}")
```

---

# Day 2 — Conditions

## Basic Theory

Conditions help a program make decisions. In real software, not every action is the same for every user. A program often needs to check whether something is true or false before continuing.

Conditional statements are used when you want the program to behave differently based on input or data.

Important ideas:

* `if` checks a condition
* `elif` checks another condition if the first one is false
* `else` runs when no condition is true
* logical operators combine multiple conditions

## Topics

* if
* elif
* else
* logical operators

---

## If Statement

Example:

```python
marks = 85

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
else:
    print("Fail")
```

---

## Nested Condition

Nested conditions are conditions inside another condition.

Example:

```python
cgpa = 3.5
income = 40000

if cgpa >= 3.5:
    if income < 50000:
        print("Eligible")
```

---

## Logical Operators

Logical operators help combine conditions.

* `and` means both conditions must be true
* `or` means at least one condition must be true
* `not` reverses a condition

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

---

## Practice

* Odd Even
* BMI
* Login System

Project:
University Result Analyzer

---

# Day 3 — Loops

## Basic Theory

Loops are used when you want to repeat a task multiple times. Instead of writing the same code again and again, loops allow the computer to do the repetition for you.

Loops are very important in automation because many tasks involve repeated actions such as processing files, checking data, or printing reports.

Important ideas:

* `for` loop is used when you know how many times to repeat
* `while` loop is used when repetition depends on a condition
* `break` stops the loop
* `continue` skips the current step and moves to the next one

## Topics

* for
* while
* break
* continue

---

## For Loop

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## While Loop

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Break

Example:

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

---

## Continue

Example:

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

## Practice

* Multiplication table
* Prime checker
* Guess Game

Project:
Quiz App

---

# Day 4 — Functions

## Basic Theory

Functions are reusable blocks of code. They help you organize your program into smaller parts so that the code becomes easier to read, test, and reuse.

Functions are one of the most important concepts in programming because they reduce repetition and make your code cleaner.

Important ideas:

* A function performs a task
* Parameters are inputs to a function
* Return gives back a result
* Functions improve readability and maintainability

## Topics

* Function
* Parameter
* Return

---

## Function Example

```python
def greet(name):

    return f"Hello {name}"

print(greet("Mayan"))
```

---

## Calculator Example

```python
def add(a, b):

    return a + b

print(add(10, 20))
```

---

## Practice

* GPA
* Tax
* Temperature

Project:
Banking App

---

# Day 5 — Data Structures

## Basic Theory

Data structures are ways to store and organize data. In Python, different data structures are used for different purposes.

Choosing the right data structure helps you write better and faster programs.

Important ideas:

* `list` stores ordered and changeable items
* `dictionary` stores key-value pairs
* `tuple` stores ordered but unchangeable items
* `set` stores unique items only

## Topics

* List
* Dictionary
* Tuple
* Set

---

## List

Lists are used when you want to store multiple values in order.

Example:

```python
students = ["A", "B", "C"]

print(students[0])
```

---

## Dictionary

Dictionaries are used when you want to store data with labels or keys.

Example:

```python
student = {

"name": "Mayan",
"cgpa": 3.90

}

print(student["name"])
```

---

## Tuple

Tuples are similar to lists, but their values cannot be changed after creation.

Example:

```python
coordinates = (10, 20)

print(coordinates[0])
```

---

## Set

Sets store unique values only.

Example:

```python
numbers = {1, 1, 2, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

---

## Practice

* Highest GPA
* Duplicate remover

Project:
Student Database

---

# Day 6 — Files & Errors

## Basic Theory

Programs often need to save data permanently. If data is only stored in memory, it disappears when the program stops. File handling allows you to read and write data from files.

Error handling is also important because programs can fail for many reasons. Instead of crashing, a good program should handle errors gracefully.

Important ideas:

* `read` gets data from a file
* `write` saves data to a file
* `append` adds new data without deleting old data
* `try` and `except` help handle errors safely

## Topics

* read
* write
* append
* try except

---

## Write

Example:

```python
file = open("notes.txt", "w")

file.write("Hello")

file.close()
```

---

## Read

Example:

```python
file = open("notes.txt")

print(file.read())

file.close()
```

---

## Append

Example:

```python
file = open("notes.txt", "a")

file.write("\nNew line")

file.close()
```

---

## Error Handling

Example:

```python
try:

    x = 10 / 0

except:

    print("Error")
```

---

## Practice

* Save notes
* Read text
* Expense logging
* Login attempts

Project:
Expense Tracker

---

# Day 7 — Modules + OOP

## Basic Theory

As programs grow larger, they become harder to manage if everything is written in one file. Modules and object-oriented programming help organize code into smaller, reusable parts.

Important ideas:

* Modules let you split code into separate files
* `import` allows you to use code from another file
* Classes are blueprints for creating objects
* Objects are real instances of a class
* OOP helps structure larger applications

## Topics

* import
* class
* object

---

## Module Example

math_tools.py

```python
def add(a, b):

    return a + b
```

main.py

```python
import math_tools

print(
math_tools.add(2, 3)
)
```

---

## Class Example

```python
class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Mayan")

print(student1.name)
```

---

## Practice

* Bank Account
* Library System

Project:
CLI Student Management System

---

# Common Python Mistakes

## 1. Using `=` Instead of `==` in Conditions

Wrong:

```python
if x = 5
```

Correct:

```python
if x == 5
```

---

## 2. Using the Wrong Variable Name

Wrong:

```python
print(Name)
```

Correct:

```python
print(name)
```

---

## 3. Forgetting to Convert Input

Wrong:

```python
age = input("Enter age: ")
print(age + 1)
```

Correct:

```python
age = int(input("Enter age: "))
print(age + 1)
```

---

## 4. Not Closing Files

Wrong:

```python
file = open("notes.txt", "w")
file.write("Hello")
```

Better:

```python
file = open("notes.txt", "w")
file.write("Hello")
file.close()
```

---

# My Learning Rules

* Build every day
* Push code to GitHub
* Read errors
* Avoid copy paste
* Finish before improving

---

# End Goal

After these 7 days I can:

✔ Write Python programs
✔ Build CLI projects
✔ Store data
✔ Organize code
✔ Prepare for APIs and Automation

Next Step:
Week 2 → APIs + JSON + Automation
