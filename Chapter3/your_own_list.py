# youownlist.py
# Exercise 3-3. From the book Python Crash Course 2nd Edition by Erick Matthews
# Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series 
# of statements about these items, such as “I would like to own a Honda motorcycle.”

my_list = '''laptop van motorbike house python gdscript piano'''.split()

print(f"I'd like to own a giant {my_list[3]} near a lake.")
print(f"I need to buy a new {my_list[0]} next year.")
print(f"I'd like to drive a {my_list[2]} some day.")
print(f"I want to learn to play {my_list[-1]} before i hit 45.")
print(f"I want to buy a {my_list[1]} and go on a roadtrip in it.")
print(f"I want to master {my_list[-3].title()} and {my_list[-2].title()} and write super awesome apps and games.")