# Exercise 4-11. From the book Python Crash Course 2nd Edition by Erick Matthews

# Start with your program from Exercise 4-1 (page 56). 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, 
# and then use a for loop to print the first list. 

# Print the message My friend’s favorite pizzas are:, 
# and then use a for loop to print the sec-ond list. 
# Make sure each new pizza is stored in the appropriate list.

my_pizzas = ["Neapolitan Pizza", "Sicillian Pizza", "Greek Pizza", "Pepperoni Pizza"]

friends_pizzas = my_pizzas[:]

my_pizzas.append('Margherita Pizza')
friends_pizzas.append('Pineapple Pizza')

print(f"My favourite pizzas are: ")
for i in my_pizzas:
    print(i)


print(f"\nMy friend's favourite pizzas are: ")
for i in friends_pizzas:
    print(i)