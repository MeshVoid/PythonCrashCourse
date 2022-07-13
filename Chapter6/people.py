# Exercise 6-7. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.

william = {
    'name': 'William',
    'last name': 'Wallace',
    'age': '35',
    'country': 'Scotland',
    'city': 'Elderslie'
}

maksat = {
    'name': 'Maksat',
    'last name': 'Bakhamov',
    'age': '45',
    'country': 'New Zealand',
    'city': 'Gondor'
}

billie = {
    'name': 'Billie',
    'last name': 'Smith',
    'age': '32',
    'country': 'India',
    'city': 'New Dheli'
}

people = [william, maksat, billie]

for person in people:
    print(f"\nPerson's name is: {person['name']}")
    print(f"Person's name is: {person['last name']}")
    print(f"Person's name is: {person['age']}")
    print(f"Person's name is: {person['country']}")
    print(f"Person's name is: {person['city']}")

