import json
import os

FILE_NAME = "passwords.json"

def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_passwords(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    data = load_passwords()
    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("Password saved successfully!")

def get_password():
    website = input("Website: ")

    data = load_passwords()

    if website in data:
        print(f"Username: {data[website]['username']}")
        print(f"Password: {data[website]['password']}")
    else:
        print("No entry found!")

while True:
    print("\n--- Password Manager ---")
    print("1. Add Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
