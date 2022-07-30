# Exercise 10-13. From the book Python Crash Course 2nd Edition 
# by Erick Matthews

# Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for
# the first time. We should modify it in case the current user is not the
# person who last used the program. 
# 
# Before printing a welcome back message in greet_user(), ask the user if this
# is the correct username. If it’s not, call get_new_username() to get the
# correct username

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

def get_stored_username():
    """Get stored username if available."""
    filename = "Chapter10/username.json"
    try: 
        with open(filename) as file: # open usernam.json, if the file exist read it into memory
            username = json.load(file) 
    except FileNotFoundError: # If file doesn't exist we prompt the user to enter their username
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?\n")
    filename = 'Chapter10/username.json'
    with open(filename, 'w') as file: 
        json.dump(username, file) 
    return username

def greet_user():
    """Check is the username is valid"""
    username = get_stored_username()
    if username:
        print(f"Hello, do you wish to log in as: {username}? y/n") 
        user_response = input()
        if user_response.lower()[0] == 'y':
            print(f"Welcome back, {username}!") # welcome user
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")

greet_user()