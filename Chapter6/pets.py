# Exercise 6-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# Pets: Make several dictionaries, where each dictionary represents a different pet.
#  In each dictionary, include the kind of animal and the owner’s name. Store these 
# dictionaries in a list called pets. Next, loop through your list and as you do, 
# print everything you know about each pet.

cat = {'species' : 'f catus', 'name': 'pussy', 'age': 12}
dog = {'species': 'canis', 'name': 'butcher', 'age': 3}
pig = {'species': 's. domesticus', 'name': 'Pinky', 'age': 4}

pets = [cat, dog, pig]


for animal in pets:
    print(f"\nPet's name: {animal['name'].title()}")
    print(f"Pet's species: {animal['species'].title()}")
    print(f"Pet's age: {animal['age']}")