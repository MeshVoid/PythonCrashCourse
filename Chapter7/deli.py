# Exercise 7-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# Deli:
#  Make a list called sandwich_orders and fill it with the names of various sandwiches.
#  Then make an empty list called finished_sandwiches. Loop through the list of sandwich
#  orders and print a message for each order, such as I made your tuna sandwich. As each
#  sandwich is made, move it to the list of finished sandwiches. After all the sandwiches
#  have been made, print a message listing each sandwich that was made.

sandwich_orders = ['egg sandwich', 'turkey sandwich',
                   'ham sandwich', 'grilled chicken sandwich']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I just made you your {sandwich}!")
    finished_sandwiches.append(sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"Today I made: {sandwich}")