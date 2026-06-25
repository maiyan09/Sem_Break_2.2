import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

api_key  = os.getenv("news_api")

def News_About_Top_business():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"
    news = requests.get(url)
    data = news.json()
    if news.status_code != 200:
        print("Error:", data.get("message"))
        return
    # print(json.dumps(data, indent=4))
    
    for article in data["articles"]:
        print(f"Source: {article['source']['name']}")
        print(f"Author: {article['author']}")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Content: {article['content']}")
        print(f"Published At: {article['publishedAt']}")
        print()
    

def News_About_Tesla():
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-05-25&sortBy=publishedAt&apiKey={api_key}"
    news = requests.get(url)
    data = news.json()
    
    if news.status_code != 200:
        print("Error:", data.get("message"))
        return
    
    for article in data["articles"]:
        print(f"Source: {article['source']['name']}")
        print(f"Author: {article['author']}")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Content: {article['content']}")
        print(f"Published At: {article['publishedAt']}")
        print()
        
while True:
    print("1. All articles about Tesla from the last month, sorted by recent first")
    print("2. Top business headlines in the US right now")
    print("3. Exit.")
    
    n = int(input("Enter you choice: "))
    
    if n == 1:
        News_About_Tesla()
    elif n == 2:
        News_About_Top_business()
    elif n == 3:
        break