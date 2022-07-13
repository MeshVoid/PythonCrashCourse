# FUNCTIONS

Functions - named blocks of code that are designed to run a specific set of instructions set by a user.
You **_call_** functions to perform a articular tasks that you earlier defined in it. 

Functions are great because they allow you not to retype the lines of code over and over again to do the same task. Using functions makes your programs easier to write, read, test and fix.

In this chapter we will learn how to call, define, pass information to functins. We will also learn how to store functions in separate files called modules to help organize our main program files.

## Defining a function

Here's a simple example of a function:

```python
#greeter.py
def greet_user(): # function definition
    """Display a simple greeting.""" # body of function
    print("Hello!")

greet_user() # calling a function
```

## Passing information to a function

If we modify the function from the abovementioned example, we can also pass information to it.

Example:
```python
def greet_user(username):
    """Display a simplt greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

The variable named username in the example above is a **parameter** of a function. The value 'jesse' is an **argument**

# Passing arguments to functions

Function definition can have multiple parameters, so that is why a function can have multiple arguments.

You can pass arguments to your functions in several ways. 

**Positional arguments** - need to be in the same order the parameters were written.

**Keyword arguments** - each argument consists of a variable name and a value, lists and dictionaries of values.

## Positional arguments

When you call a function, Python must match each argument in the function call with a parameter in the 
function definition. The simplest way to do this is based on the order of the arguments provided.
Values matched up this way are called _positional arguments_.

An example of using **positional arguments**.
```python
#pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

## Multiple function call

You can call a function as many times as needed. Describing a second, different pet requires just one more
call to describe_pet():
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'william')

```
Calling a function multiple times is a very efficient way to work as the code written in the function won't have to be rewritten again and again. 

## Order matters in positional arguments

When dealing with positional arguments in a function you can get unexpected results if you miss the order of the arguments in a function call:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
```
To avoid getting funny results like that check to make sure that the order of arguments in your function calls matches the parameters in the function's definition.

## Keyword arguments

**A keyword argument** is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion.

**Keyword arguments** free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```
The order of keyword arguments doesn't matter because Python knows where each value should go.

The following function calls are the same:

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```
_When you use keyword arguments make sure that those are EXACT same names of the parameters in the function definition_

## Default values

When writing a function, you can define a **default value** for each parameter. 
Using default values can simplify your function calls and clarify the ways in which your functions are typically used.

Example:
```python
def describe_pet(pet_name, animal_type ='dog'): # order of parameters has to be changed
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Larry')
```
_When you use default values, any parameter with a default value needs to be listed AFTER all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly_

## Equivalent function calls

```python
def describe_pet(pet_name, animal_type='dog'):
```

All following calls would work for this function:

```python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry') 
```

_It doesn't really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand._

## Avoiding argument errors

When you start to use functions, don't be surprised if you encounter errors about unmatched arguments.

Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.


```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet() # This will cause an argument error
```

# RETURN VALUES IN FUNCTIONS

A funcition doesn't have to display its output directly. Instead, it can just process some data and then return a value or set of values.

_**Return value**_ - value that is returned by a function. 

## Returning a simple value

Example:
```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmie', 'hendrix')
print(musician)
```

# Making an argument optional

Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional.

```python
def get_formatted_name(first_name, last_name, middle_name =''): # we assign an empty value to make it optional
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmie', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker','lee')
print(musician)
```
_Optional values allow functions to handle a wide range of use cases while letting function calls remain as simple as possible._

## Returning a dictionary

A function can return any type of value you need it to, including lists and dictionaries. 

Example:
```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', "hendix")
print(musician)



# allow storing age as well

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', "hedrix", age = 34)
print(musician)
```


## Using a function with a while loop

You can use funcitons with all the Python structures you've learned about so far.

For example, let's use the get_formatted_name() function with a while loop to greet
users more formally. Here's a first attempt at greeting people using their first and
last names:

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

## Passing a list

You'll often find it useful to pass a list to a function. When you pass a list to a function, the function gets direct access to the contents of the list. Let's use functions to make working with lists more efficient.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
```


## Modifying a list in a function
When you pass a list to a function, the function can modify the list. Any chages made to the list inside the function's body are permanent, allowing you to work efficiently even when you're dealing with large amounts of data.


Program without functions:
```python
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

The same program but structured into functions:
```python
#printing_models.py
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```
This program is easier to extend and maintain than the version with-out functions. If we need to print more designs later on, we can simply call print_models() again. If we realize the printing code needs to be modified, we can change the code once, and our changes will take place everywhere the function is called.

This example also demonstrates the notion that a function should have one specific job.

## Prevent a function from modifying a list

Sometimes you'll want to prevent a function from modifying a list. To do so you can pass a **copy of a list** to a function NOT THE ORIGINAL!

To do it you will have to call a function like this:
```python
function_name(list_name[:])
```
The slice notation [:] makes a copy of the list to send to the function.

Even though you can preserve the contents of a list by passign a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy.


## Passing an arbitrary number of arguments

Sometimes you don't know how many arguments a function will need to accept as you are in the process of writing it.

Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

```python
def make_pizza(*toppings): # we use * before the argument
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")
```
The aterisk * symbol before the argument name tells Python to make an empty tuple called **toppings** and pack whatever values it receives into a tuple.

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")
```
This syntax with an asteriks and an argument name - *argument_name. Works no matter how many arguments the function receives.

## Mixing positional and arbitrary arguments


If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary amount of arguments must be placed last in the function definition.

Python always matches positional arguments first and then collects any remaining arguments in the final paramenter.

EXAMPLE:
```python
# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms","green peppers","extra cheese")
```
_You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this._


## Using arbitrary keyword arguments

Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of information will be passed to the function.

In this case, you can write functions that accept as many key-value pairs as the calling statement provides.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)
```

We indicate arbitrary arguments with _**argument_, you will often see the parameter name **kwargs used to collect non-specific keyword arguments. ** - makes dictionary out of arbitrary arguments


# Storing your functions in modules