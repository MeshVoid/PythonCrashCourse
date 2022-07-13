# USER INPUT AND WHILE LOOPS

_In this chapter we will learn hot to get user input using the **input()** function and how to keep a program running as long as a certain conditions remain true using **while loop**._

## How the input() function works

The input() function pauses your program and waits for the user to enter some text.
Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.

Example:
```python
#parrot.py
message = input("Tell me something, and I will repeat it back to you: ") 
# input() takes one argument - prompt mesage
print(message)
```

The input() function takes one argument: the prompt, or instructions, that we want to display to the user so they know what to do. In this example, when Python runs the first line, the user sees the prompt Tell me something, and I will repeat it back to you: . The program waits while the user enters their response and continues after the user presses enTer. The response is assigned to the variable message, then print(message) displays the input back to the user.


## Writing clear prompts

Each time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of informatin you're looking for.

```python
# greeter.py
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

Sometimes you'll want to write a prompt that's longer than one line.
Example:
```python
prompt = "If you tell us who you re, we can personalize the messages you see."
prompt += "\nWhat is your first name? "# use += to add a new string to the end

name = input(prompt)
print(f"\nHello, {name}!")
```

## Using int() to accept numerial input

 The **int()** function, which tells Python to treat the input as a numerical value. The int() function con-verts a string representation of a number to a numerical representation, as shown here:

```python
age = input("How old are you? ")
age = int(age)
age > = 18 # returns true
```

Another example:
```python
#rollercoaster.py
height = input("How tall are you, in cm? ")
height = int(height)

if height >= 158:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

## The Modulo Operator

A useful tool for working witn numerical information is the modulo operator **(%)**.
This operator divides one number by another number and returns the remainder

The modulo number doesn't tell you how many times one number fits into another; it
just tells you what the remainded is.

You can easily use (%) modulo operator to determine if a number is even or odd:

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
```

# Introducing while loops

The for loop takes a collection of items and executes a block of code once for each item in the collection.
In contrast, the while loop runs as long as, or while, a certain condition is true.

## The while loop action.

You can use a while loop to count up through a series of numbers:
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

## Letting the user choose when to quit

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != 'quit':
        print(message)
```


## Using a flag

There may be different events that could cause the program to stop running. For a program that should run only as long
as many conditions are true, you can define one variable that determines whether or not the entire program is active.

This variable called _**flag**_ acts as a signal to the program. We can write our programs so they run while the flag
is set to True and stop running when any of several events sets the value of the flag to False.

This is how it would look like:
```python

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

_Using a flag for a while loop is useful in complicated programs like games, where there may be many events that should each make the program stop running._

## Using break to exit a loop

To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any 
conditional test, use the _**break**_ statement.

The break statement directs the flow of your program, you can use it to control which lines of code are executed and
which are not. 

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

_You can use the break statement in any of Python's loops. For example, you could use **break** to quit a **for loop** that's working through a list or a dictionary._

## Using continue in a loop

Instead of breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

```python
current_number = 0

while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # skip through even numbers
    print(current_number)
```


## Avoiding infinite loops

Sometimes you can make a mistake and make a while loop run forever.
Everyone accidentally writes an infinite while loop from time to time, especially when program's loops has subtle exit conditions.

Press CTRL + C to exit the loop or close a terminal\console window you're running your program in.

## Using a while loop with lists and dictionaries

To keep track of many users and pieces of information, we will need to use lists and dictionaries with
our while loops.

A for loop is effective for looping through a list, but you shoudn't modify a list inside a for loop
because Python will have trouble keeping track of the items in the list. To modify a list it is way better
to use a while loop. Using while loops with lists and dictionaries allows you to collect, store and organize lots of input to examine and report on later.

## Moving items from one list to another

To move items from one list to another we could use a _**while loop**_ to pull entries from one list and add them to another. 

Here's an example:

```python
# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# Verify each user until there are no more unconfimed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

## Removing all instances of specific values from a list

We used remove() previously in Chapter 3, we used it to remove single items, but what if you want to remove
all instances of the same value from the list?

Here's an example:
```python
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets: # check if there is a value 'cat' in the list pets
    pets.remove('cat')

print(pets)
```

## Filling a dictionary with user input

You can prompt for as much input as you need in each pass through a while loop. Let's make a polling program in which each pass through the loop prompts for the participant's name and response.

```python
responses = {} # declare empty dictionary

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    
    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")
```