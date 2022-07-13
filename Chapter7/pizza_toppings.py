# Exercise 7-4. From the book Python Crash Course 2nd Edition by Erick Matthews

# Pizza Toppings:Write a loop that prompts the user to enter a series of pizza 
# toppings until they enter a 'quit' value. As they enter each topping, print a 
# message saying you’ll add that topping to their pizza.

prompt = "\nHello there, please enter what kind of pizza toppings would you like to be served!"
prompt += "\n(Type 'quit' to exit the program)\n"

while True:
    user_input = input(prompt)

    if user_input.lower() == 'quit':
        break
    else:
        print(f"Okay, I will add {user_input} as your pizza topping!")

