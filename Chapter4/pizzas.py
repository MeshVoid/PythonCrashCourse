# Pizzas.py by Chingiz Jumagulov

# Execise 4-1. From the book Python Crash Course 2nd Edition by Erick Matthews
# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
# and then use a for loop to print the name of each pizza.

# Modify your for loop to print a sentence using the name of the pizza instead of 
# printing just the name of the pizza. For each pizza you should have one line of 
# output containing a simple statement like I like pepperoni pizza.


# Add a line at the end of your program, outside the for loop, that states how much you 
# like pizza. The output should consist of three or more lines about the kinds of pizza 
# you like and then an additional sentence, such as I really love pizza!

# Added beer to the mix, because why the hell not, lol

pizza_names = ["Neapolitan Pizza", "Sicillian Pizza", "Greek Pizza", "Pepperoni Pizza"]

for pizza in pizza_names:
    print(f"I love to munch on that {pizza} every single day!")

print("\nI do really hope I don't get that colon cancer eating all that fat food all day long!\n")


beer_types = ["Ale", "Lager", "Stout", "Pilsner", "Porter", "Lager"]

for beer in beer_types:
    print("Boy oh boy am I ready for that beer tonight!")
    print(f"Okay, bartender, my dude, I'll have one {beer} please! Thanks!")

print("\nMy head hurts from all that beer I drank yesterday, damn!")
print("Shit, test result are here. FUCK! I do have colon cancer tho. Damn...")
