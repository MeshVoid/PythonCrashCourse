# Exercise 4-13. From the book Python Crash Course 2nd Edition by Erick Matthews

# Buffet: A buffet-style restaurant offers only five basic foods.

# Think of five simple foods, and store them in a tuple.

# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the change.
# • The restaurant changes its menu, replacing two of the items with different foods.
#   Add a line that rewrites the tuple, and then use a for loop to print each
#   of the items on the revised menu.


foods = ('pelmeni', 'pirozhki', 'scrambled eggs',
         'boiled potatoes', 'fried grubs')
print(foods)

# Try to modify one of the items, and make sure that Python rejects the change.
# foods[1] = 'ice cream'

foods = ('ice cream', 'meat pies', 'scrambled eggs',
         'boiled potatoes', 'fried grubs')
print(foods)
for food in foods:
    print(food)
