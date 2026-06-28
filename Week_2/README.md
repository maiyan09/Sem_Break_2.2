# Python Second 7 Days — APIs, Automation & Real Projects

Author: maiyan09
Goal: Use Python to interact with external systems, automate tasks, and prepare for AI development.

---

# Introduction

The first 7 days focused on learning Python itself.

The second 7 days focus on using Python to solve real-world problems.

Main goals:

* Organize Python projects
* Work with JSON
* Consume APIs
* Automate repetitive tasks
* Extract information from websites
* Build complete applications

Rule:

Learn → Build → Publish → Reflect

---

# Day 8 — Professional Python Setup

## Basic Theory

As projects grow, organization becomes important.

Professional developers separate environments and dependencies to avoid conflicts.

Important ideas:

* Virtual Environment (venv)
* Package Manager (pip)
* Dependency Management
* Project Structure

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

---

## Install Packages

```bash
pip install requests
```

Save packages:

```bash
pip freeze > requirements.txt
```

Install later:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
student_app/

main.py
utils.py
requirements.txt
README.md
```

---

## Practice

1. Create venv
2. Install package
3. Freeze dependencies
4. Import local module

---

## Mini Project

Build:

Student Utility Package

Modules:

```text
add.py
search.py
main.py
```

---

# Day 9 — JSON & Data Exchange

## Basic Theory

JSON (JavaScript Object Notation) is the standard format for exchanging data.

Most APIs send and receive JSON.

Example JSON:

```json
{
    "name":"Mayan",
    "cgpa":3.80
}
```

---

## Convert Dictionary → JSON

```python
import json

student = {
    "name":"Alex",
    "cgpa":3.9
}

print(
json.dumps(student)
)
```

---

## JSON → Dictionary

```python
import json

data='{"name":"Sam"}'

result=json.loads(data)

print(result["name"])
```

---

## Save JSON File

```python
import json

data={
"name":"A"
}

with open(
"data.json",
"w"
) as file:

    json.dump(
        data,
        file
    )
```

---

## Read JSON

```python
with open(
"data.json"
) as file:

    data=json.load(file)

print(data)
```

---

## Practice

1. Student JSON
2. Product catalog
3. Course data

---

## Mini Project

Student Record Manager

Features:

* Add
* Save
* Load
* Search

---

# Day 10 — APIs (Core Skill)

## Basic Theory

API means Application Programming Interface.

It allows programs to communicate.

Example:

```text
Python → API → Server → Response
```

HTTP Methods:

* GET → Read
* POST → Send
* PUT → Update
* DELETE → Remove

Status Codes:

* 200 OK
* 404 Not Found
* 500 Server Error

---

## Install Requests

```bash
pip install requests
```

---

## First API Request

```python
import requests

url="https://api.github.com"

response=
requests.get(url)

print(
response.status_code
)
```

---

## Read JSON Response

```python
data=
response.json()

print(data)
```

---

## Error Handling

```python
if response.status_code==200:

    print("Success")

else:

    print("Failed")
```

---

## Practice

1. Country Info
2. Random User
3. Weather Data

---

## Mini Project

Country Information App

Input:

Country Name

Output:

Capital
Population
Currency

---

# Day 11 — Automation Scripts

## Basic Theory

Automation means reducing manual work.

Python is powerful because it can automate:

* Files
* Reports
* Data cleaning
* Renaming
* Scheduling

---

## Rename Files

```python
import os

files=
os.listdir()

for i,file in enumerate(files):

    os.rename(
        file,
        f"file_{i}.txt"
    )
```

---

## Create Folder

```python
import os

os.mkdir(
"Reports"
)
```

---

## Practice

1. Organize files
2. Rename images
3. Generate folders

---

## Mini Project

Automatic File Organizer

Features:

* Sort
* Move
* Rename

---

# Day 12 — Web Scraping

## Basic Theory

Web scraping extracts information from web pages.

HTML structure:

```html
<h1>Title</h1>
<p>Paragraph</p>
```

Libraries:

* requests
* BeautifulSoup

Install:

```bash
pip install beautifulsoup4
```

---

## First Scraper

```python
import requests

from bs4 import BeautifulSoup

html=
requests.get(
"https://example.com"
)

soup=
BeautifulSoup(
html.text,
"html.parser"
)

print(
soup.title.text
)
```

---

## Find Elements

```python
items=
soup.find_all("p")

for item in items:

    print(item.text)
```

---

## Practice

1. Headlines
2. Table extraction
3. Links

---

## Mini Project

University Notice Collector

---

# Day 13 — Real Automation Project

## Objective

Combine previous knowledge.

Build:

Student Result Processor

Features:

* Read JSON
* Analyze
* Save Report

---

## Example

```python
students=[
80,
70,
90
]

avg=
sum(students)/len(
students
)

print(avg)
```

---

## Deliverables

README

Screenshots

Documentation

---

# Day 14 — Capstone Project

## Build

Student Analytics Dashboard

Features:

* Import Data
* Analyze
* Export Report
* Statistics

---

## Suggested Structure

```text
dashboard/

data/

main.py

utils.py

report.py

README.md
```

---

# Debugging Tips

1.

Use:

```python
print(variable)
```

---

2.

Read errors fully.

---

3.

Search exact errors.

---

4.

Fix one problem at a time.

---

# GitHub Publishing Checklist

Include:

* README
* Installation
* Usage
* Screenshots
* Features
* Lessons Learned

Example:

```text
git add .

git commit -m
"Complete Day 14"

git push
```

---

