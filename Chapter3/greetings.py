# Greetings.py
# Exercise 3-2. From the book Python Crash Course 2nd Edition by Erick Matthews
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
# print a message to them. The text of each mes-sage should be the same, but each message should 
# be personalized with the person’s name.
import random

names = ['ruslan','shyako','maksutbek']

def greetings():
        print(f"Hello there, {names[0].title()}! Why r u gae?")
        print(f"Howdie there, {names[1].title()}! Why r u not gae?")
        print(f"'Allo there, {names[2].title()}, mate! Do you know da wae?")

greetings()