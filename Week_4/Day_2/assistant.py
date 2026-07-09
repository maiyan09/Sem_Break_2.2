import os
import json
import pandas as pd
from dotenv import load_dotenv
from google import genai
from datetime import datetime
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

file_name = "history.json"
class StudyAssistant:
    def __init__(self):
        print("\nStudy Assistant is ready!")
        
    def ask_question(self):
        print("Enter your Question.\n> ", end="")
        ques = input()
        return ques
    def get_ai_response(self, question):
        try:
            prompt = f"""
                You are a friendly study assistant.

                Rules:
                - Explain concepts simply.
                - Use beginner-friendly language.
                - Give examples whenever possible.
                - If appropriate, use Python examples.
                - Use as less possible token

                Student Question:
                {question}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except Exception as e:
            return f"Error: {e}"
        
    def save_history(self, question, answer):
        try:
            # load existing history
            with open(file_name, "r") as file:
                history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty
            history = []
        history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
    
    def clear_history(self):
        try:
            with open(file_name, "w") as file:
                json.dump([], file, indent=4)
            print("History cleared.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No history found.")
    
    def export_history(self):
        try:
            with open(file_name, 'r') as file:
                history = json.load(file)
                
            df = pd.DataFrame(history)
            df.to_csv("history.csv", index = False)
            print("Chat History Export Successfully.")
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("No history found.")