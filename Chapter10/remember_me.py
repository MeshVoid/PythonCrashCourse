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
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!") # welcome back if username exists
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()