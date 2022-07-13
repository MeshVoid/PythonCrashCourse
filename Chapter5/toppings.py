requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False

print("\n")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# If used if-elif then this code wouldn't work:

print("\n")

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
# We didn't get out extra cheese on our pizza!
print("\nFinished making your pizza!")

# using for loop with our list
print("\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# using for if statement in a for loop to check for special items in the list

print("\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")


print("\nFinished making your pizza!")

# We can can use if statement to quickly check if a list has any entries and is not empty before running a for loop

print("\n")

requested_toppings = []  # empty list

if requested_toppings:  # empty list returns False
    for requested_topping in requested_toppings:  # this block will be omitted because the list is empty
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:  # this will be printed instead
    print("Are you sure you want a plain pizza?")


# Using if statement with multiple lists:

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

print("\n")

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")