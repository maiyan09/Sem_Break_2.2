# Study Assistant 📚

A simple Python command-line application that helps users ask study-related questions, save conversations, view previous history, and export the history to a CSV file.

This project was built to practice Python programming, Object-Oriented Programming (OOP), file handling, JSON, and CSV export.

---

## Features

* Ask study-related questions
* Get predefined AI responses
* Save every conversation automatically
* View all previous conversations
* Export conversation history to a CSV file
* Handles missing or empty history files safely

---

## Project Structure

```text
StudyAssistant/
│
├── main.py          # Runs the application
├── assistant.py     # Contains the StudyAssistant class
├── history.json     # Stores conversation history
├── history.csv      # Exported conversation history
└── README.md
```

---

## Technologies Used

* Python
* JSON
* CSV
* Pandas (for CSV export)

---

## How It Works

1. Run the program.
2. Choose an option from the menu.
3. Ask a question.
4. The assistant searches for the answer from its predefined knowledge.
5. The question and answer are saved in `history.json`.
6. You can view previous conversations.
7. You can export the history to `history.csv`.

---

## Menu

```text
1. Ask Question
2. View History
3. Export History
4. Exit
```

---

## Example

### Ask a Question

```text
Enter your Question:
> what is python

Python is a programming language.
```

---

### View History

```text
Conversation 1

Question:
what is python

Answer:
Python is a programming language.
```

---

### Export History

After choosing **Export History**, a file named `history.csv` is created.

Example:

| question       | answer                                 |
| -------------- | -------------------------------------- |
| what is python | Python is a programming language.      |
| what is ai     | AI stands for Artificial Intelligence. |

---

## Concepts Practiced

This project helped me practice:

* Classes and Objects
* Functions
* Dictionaries
* Lists
* Loops
* Exception Handling
* File Handling
* JSON
* CSV Export
* Basic Project Structure

---

## Future Improvements

Some ideas to improve this project:

* Connect to a real AI API
* Search conversation history
* Delete conversations
* Edit previous conversations
* Add timestamps
* Export to PDF
* Build a graphical user interface (GUI)
* Store data in a database like SQLite

---

## Author

Created by **maiyan09** as a Python learning project.
