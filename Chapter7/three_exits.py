# Exercise 7-6. From the book Python Crash Course 2nd Edition by Erick Matthews

# Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:

# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nHello there, please enter what kind of pizza toppings would you like to be served!"
prompt += "\n(Type 'quit' to exit the program)\n"

user_input = ''

while user_input != 'quit':
    user_input = input(prompt)
    if user_input != 'quit':
        print(f"Okay, I will add {user_input} as your pizza topping!")