import json
import pandas as pd

file_name = "history.json"
class StudyAssistant:
    def __init__(self):
        print("\nStudy Assistant is ready!")
        
        self.answers = {
            "what is python": "Python is a programming language.",
            "what is ai": "AI stands for Artificial Intelligence.",
            "what is computer": "A computer is an electronic machine that processes data."
        }
        
    def ask_question(self):
        print("Enter your Question.\n> ", end="")
        ques = input()
        return ques
    
    def get_ai_response(self, question):
        if question in self.answers:
            return self.answers[question]
        else:
            return "Sorry, I don't know the answer."
        
    def save_history(self, question, answer):
        try:
            # load existing history
            with open(file_name, "r") as file:
                history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty
            history = []
        history.append({
            "question": question,
            "answer": answer
        })
        # Converting Python → JSON file
        with open(file_name, 'w') as file:
            json.dump(history, file, indent=4)
            
    def view_history(self):
        try:
            with open(file_name, 'r') as file:
                viewHistory = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        return viewHistory
    
    def export_history(self):
        try:
            with open(file_name, 'r') as file:
                history = json.load(file)
                
            df = pd.DataFrame(history)
            df.to_csv("history.csv", index = False)
            print("Chat History Export Successfully.")
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("No history found.")