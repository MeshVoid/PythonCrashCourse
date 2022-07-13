name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# prompt longet than one line:

prompt = "If you tell us who you re, we can personalize the messages you see."
prompt += "\nWhat is your first name? " # use += to add a new string to the end

name = input(prompt)
print(f"\nHello, {name}!")