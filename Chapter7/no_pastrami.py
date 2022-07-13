# Exercise 7-9. From the book Python Crash Course 2nd Edition by Erick Matthews

# No Pastrami: 
# Using the list sandwich_orders from Exercise 7-8, make sure the 
# sandwich 'pastrami' appears in the list at least three times. Add code near 
# the beginning of your program to print a message saying the deli has run out
# of pastrami, and then use a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami sandwiches 
# end up in finished_sandwiches.

sandwich_orders = ['egg sandwich','pastrami sandwich','turkey sandwich',
                   'ham sandwich', 'grilled chicken sandwich', 
                   'pastrami sandwich', 'pastrami sandwich']


finished_sandwiches = []

print("\nDeli has ran out of pastrami! All pastrami orders are cancelled!")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

for sandwich in sandwich_orders:
    print(f"I just made you your {sandwich}!")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"Today I made: {sandwich}")