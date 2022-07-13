# seeing_the_world.py
# Exercise 3-8. From the book Python Crash Course 2nd Edition by Eric Matthews
# Seeing the World: Think of at least five places in the world you’d like to visit.

places_to_visit = ['Machu Picchu', 'Toronto', 'Moscow', 'Cape Town', 'Barcelona']
print(f"Places to visit: {places_to_visit}")
print(f"Places to visit sorted: {sorted(places_to_visit)}") #sorted()
print(f"Places to visit original list: {places_to_visit}")
print(f"Places to visit sorted in reverse: {sorted(places_to_visit,reverse=True)}") #sorted()
print(f"Places to visit original list: {places_to_visit}")
places_to_visit.reverse()
print(f"Places to visit reversed: {places_to_visit}") #sorted()
places_to_visit.reverse()
print(f"Places to visit reversed back: {places_to_visit}") #sorted()
places_to_visit.sort()
print(f"Places to visit sort : {places_to_visit}") #sorted()
