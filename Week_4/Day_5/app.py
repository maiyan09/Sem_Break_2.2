from auth import create_token, verify_token, logout
from database import load_users, login, save_users

while True:
    print("========== MENU ==========")
    print("1. Register")
    print("2. Login")
    print("3. View Profile")
    print("4. Logout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        new_user = {
            "username": username,
            "password": password
        }

        users = load_users() # -> Load existing user from users.json
        for user in users: # -> Chekcing for duplicate
            if user["username"] == username:
                print("Username already exists.")
                break
        else:
            users.append(new_user)
            save_users(users)
            print("User registered successfully!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if login(username, password):
            create_token(username)
            print("Login Successful!")
        else:
            print("Invalid username or password.")
    elif choice == "3":
        profile = verify_token()

        if profile:
            print(f"Welcome, {profile['username']}")
            print(f"Role: {profile['role']}")
        else:
            print("Please login first.")
    elif choice == "4":
        logout()
    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice.")