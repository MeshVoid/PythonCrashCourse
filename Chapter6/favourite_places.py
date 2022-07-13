# Exercise 6-9. From the book Python Crash Course 2nd Edition by Erick Matthews
# Favorite Places: 
# Make a dictionary called favorite_places. Think of three names to use as keys 
# in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few 
# of their favorite places. Loop through the dictionary, and print each person’s 
# name and their favorite places.

favourite_places = {
    'steve': 'local Mcdonalds',
    'margareth': 'Edinburgh',
    'josh': 'Wall Street in New Yort'
}

for name, place in favourite_places.items():
    print(f"{name.title()}'s favourite place is: {place}")

    