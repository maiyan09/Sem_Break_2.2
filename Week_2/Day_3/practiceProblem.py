import requests
import json

# Fetch Public API 

url = "https://jsonplaceholder.typicode.com/posts"

try:
    info = requests.get(url)
    info.raise_for_status()
    print(info.status_code) #If it gives 200 means working
    
    users = info.json()
    print(json.dumps(users, indent=4))
 
    for user in users:
        print(f"User ID: {user['userId']}")
        print(f"ID: {user['id']}")
        print(f"Title: {user['title']}")
        
except requests.exceptions.Timeout as t:
    print(t)
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server.")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")