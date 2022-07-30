# Exercise 10-11 and 10-12. From the book Python Crash Course 2nd Edition 
# by Erick Matthews
#
# Favorite number: Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message, 
# “I know your favorite number! It’s _____.”

# Favorite Number Remembered: Combine the two programs from Exercise 10-11 
# into one file. If the number is already stored, report the favorite number 
# to the user. If not, prompt for the user’s favorite number and store it in 
# a file. Run the program twice to see that it works.

import json


def get_stored_favorite_number():
    """Check if favorite number exists and return it if it does"""
    filename = "Chapter10/favorite_number.json"
    try:
        with open(filename, 'r') as file:
            favorite_number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """Ask user to enter his favorite number, save it into a file"""
    favorite_number = input("Enter your favorite number:\n")
    filename = "Chapter10/favorite_number.json"
    with open (filename, 'w') as file:
        json.dump(favorite_number, file)

def read_favorite_number():
    """Read user's favorite number from a json file."""
    filename = "Chapter10/favorite_number.json"
    with open(filename, 'r') as file:
        favorite_number = json.load(file)
    print(f"Your favorite number is: {favorite_number}")

def main():
    print("Welcome!")
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        read_favorite_number()
    else:
        get_new_favorite_number()

main()