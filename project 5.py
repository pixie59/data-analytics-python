import pyperclip
import os
file_name="passwords.txt"
def save_password():
    website=input("Enter the website: ")
    password=input("Enter the password: ")
    with open(file_name, "a") as f:
        f.write(f"{website} <||> {password}\n")
def get_password():
    website=input("Enter the website: ")
    with open(file_name, "r") as f:
        for line in f:
            if website in line:
                pyperclip.copy(line.split(" <||> ")[1])
                print("Password copied to clipboard.")
                return
    print("Website not found.")
def main():
    while True:
        print("Password Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
main() 
