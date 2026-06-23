```md
# 🐍 Day 8 — Modules + Environment + Professional Setup

**Topic:** Python Project Structure, Virtual Environments, and Professional Workflow  
**Level:** Beginner → Foundation for Real Projects  

---

## 📌 Overview

Day 8 focuses on how real Python projects are structured and managed.

Instead of just writing code, you learn how professionals:

- Organize projects properly
- Use virtual environments
- Manage dependencies
- Create reusable modules
- Prepare projects for GitHub and production

---

## 🧠 Key Concepts

### 1. Project Structure

A clean Python project is organized like this:

```

project/
│
├── .venv/               # Virtual environment (not pushed to GitHub)
├── student_tools.py    # Your module (reusable code)
├── main.py             # Entry point
├── requirements.txt    # Dependencies list
└── README.md           # Project documentation

````

👉 Good structure = easier maintenance + professional look

---

### 2. Virtual Environment (venv)

A virtual environment isolates your project dependencies.

#### Why it matters:
- Prevents package conflicts
- Keeps projects independent
- Standard in real-world development

#### Create venv:
```bash
python -m venv .venv
````

#### Activate venv:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. pip (Package Manager)

`pip` is used to install Python libraries.

#### Example:

```bash
pip install requests
```

#### Check installed packages:

```bash
pip list
```

---

### 4. requirements.txt

This file stores all project dependencies.

#### Create it:

```bash
pip freeze > requirements.txt
```

#### Install from it:

```bash
pip install -r requirements.txt
```

👉 This allows anyone to run your project easily.

---

### 5. Imports (Using Modules)

Python allows you to split code into multiple files.

#### Example:

📁 `student_tools.py`

```python
def greet(name):
    return f"Hello {name}"

def add(a, b):
    return a + b
```

📁 `main.py`

```python
import student_tools

print(student_tools.greet("Mayan"))
print(student_tools.add(5, 10))
```

---

## 🧪 Practice Tasks

### 1. Create Virtual Environment

* Create `.venv`
* Activate it successfully

---

### 2. Install a Package

Example:

```bash
pip install requests
```

---

### 3. Freeze Requirements

```bash
pip freeze > requirements.txt
```

---

### 4. Import Own Module

* Create `student_tools.py`
* Import it in `main.py`
* Call functions successfully

---

## 🧩 Project — student_tools.py

### 🎯 Goal:

Build a reusable Python module with utility functions.

---

### 📄 student_tools.py

```python
def greet(name):
    return f"Hello, {name}! Welcome to Python."

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def is_even(number):
    return number % 2 == 0
```

---

### 📄 main.py

```python
import student_tools

print(student_tools.greet("Alex"))

nums = [10, 20, 30]
print("Average:", student_tools.calculate_average(nums))

print("Is 10 even?", student_tools.is_even(10))
```

---

## 📘 Extra Task — Professional README

Create a `README.md` for your project with:

### Must include:

* Project title
* Description
* Setup instructions
* How to run
* Features
* Example usage

---

## 📌 Example README Structure

```md
# Student Tools Project

## Description
A simple Python module for basic student utilities.

## Setup
pip install -r requirements.txt

## Run
python main.py

## Features
- Greeting function
- Average calculator
- Even number checker
```

---

## 🎯 Learning Outcome

After Day 8, you can:

✔ Create professional Python project structure
✔ Use virtual environments
✔ Manage dependencies with pip
✔ Create and import modules
✔ Write basic professional documentation

---
```
```
