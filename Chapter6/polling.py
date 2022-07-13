# Exercise 6-6. From the book Python Crash Course 2nd Edition by Erick Matthews

# Polling: Use the code in favorite_languages.py (page 97).

# • Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not. 

# • Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. If they 
# have not yet taken the poll, print a message inviting them to take the poll.


favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

must_take_poll = 'ben david chingiz mukhtar jen sarah edward phil'.split()

for people in must_take_poll:
    if people in favourite_languages.keys():
        print(f"{people.title()} already passed the poll, and is good to go home now.")
    else:
        print(f"{people.title()} is yet to pass the poll, please proceed to the interrogation room.")


