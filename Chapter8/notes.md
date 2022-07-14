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

One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a _module_ and the _importing_ that module into your main program.

An **_import_** statement tells Python to make the code in a module available in the currently running program file.

Storing funcitons separately in a different file allows you to hide the details of your program's code and focus on it's higher-level logic. 

## Importing an entire module

A _module_ is a file ending in .py that contains the code you want to import into your program.

Let's take the following function and store it in a separate file, for example:
```python
#stored in pizza_module.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```
Now, we'll make a separate file called making_pizzas.py in the same directory as pizza_module.py

```python
#file making_pizzas.py 
import pizza_module # use keyword import and the name of our py file

pizza_module.make_pizza(14, 'pepperoni') # call functions from imported module: module_name.func_name(args)
pizza_module.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

_If you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax:_
```python
module_name.function_name()
```

## Importing specific functions

You can also import a specific function from a module. Here' the general syntax for this approach:

```python
from module_name import function_name
```
You can import as many functions as you want from a module by separating each function's name with a comma:
```python
from module_name import function_0, function_1, function_2, function_3
```
Just add FROM and then indicate what to IMPORT and it'll work just as fine as it did before:
```python
from pizza_module import make_pizza

make_pizza(14, 'pepperoni') # no need for pizza_module. now!
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```

## Using 'as' to give a function alias

If the name of a function you're importing might conflict with an existing name in your program or the function name is just too long, you can use a short, unique alias - an alternate name similar to a nickname for the function.

```python
from pizza_module import make_pizza as mp # giving an alias name to the function make_pizza

mp(14, 'pepperoni') # now it's a short name mp
mp(16, 'mushrooms', 'green peppers', 'extra cheese')
```
SYNTAX:
```python
from module_name import function_name as fn
```

## Using 'as' to give a module an alias

You can also provide an alias for a module name. Giving a modle a short alias, like p for pizza, allows you to call the module's functions more quickly.

Calling p.make_pizze() is more concise that calling pizza_module.make_pizza():
```python
import pizza_module as p # giving an alias to the whole pizza_module

p.make_pizza(14, 'pepperoni')  # now it's a short name mp
p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
```
Syntax:
```python
import module_name as mn
```


## Importing all functions in a module

You can also import every single function in a module by using the asterisk (*) operator:

```python
from pizza_module import * # import all functions in a module

make_pizza(16, 'pepperoni')
```

The (*) asterisk in the import statement tells Python to copy every function from the given module into the current program file.
And because every function is imported into your file, you can call each function from the imported module without using the dot notation.

It's important to note, that it is best **not to use this approach** when you're working with larger modules that you didn't write: if a module has a function name that matches an existing name in your project, you can get some unexpected results. For example, Python may see several functions or variables with the same name and instead of importing all the functions separately, it **will overwrite the functions**.

**The best approach** is to **import the function** of functions you want, or **import the entire module** and use the dot notation. This will lead to clear code that's easy to read and understand. But it's beneficial to know the syntax so that you could recognize it somebody else's code.
Syntax:
```python
from module_name import *
```

## Styling functions

When dealing with functions make sure they have descriptive names, and these names should use lowercase letters and underscores.

Descriptive nmes help you and other understand what your code is trying to do. Module names should use these conventions as well.

Every function should have a comment that explains concisely what the function does right after the function definition and use the docsrting ''' ''' format. 

If a function is well-documented other programmers can use the function by reading only the description in the docstring. Other programmers should be able to trust that the code works as described in the function description. As long as others know the name of the function, the arguments it needs and the kind of value it returns, they should be able to use it in their programs.

If you indicate a **default value for a certain parameter, then you shouldn't use any spaces on either side of the equal sign!
Syntax:
```python
def function_name(parameter_0, parameter_1='default value')
```

The same convention should be used for keyword arguments in function calls:
```python
function_name(value_0, parameter_1='value')
```
According to PEP 8, it is recommended that you limit the lines of code to 79 characters.
If a set of parameters causes a function's definition to be too long, then press ENTER
and open parenthesis on the definition line:

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```

If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.

All **import** statements should be writter at the beginning of a file.

## Summary of Chapter 8:
Write simple code that does what you want it to, and utilise functions to do so. Functions allow you to write blocks of code and leave them alone once you know they work properly. When you're finished writing a function you can trust that it will always work and move on to your next coding task.

Functions allow you to write code once and then reuse that code as many times as you want. When you need to run the code in a function, all you need to do is write a one-line call and the function does its job. When you need to modify a function's behavior, you only have to modify one block of code, and your changes takes effect everywhere you've made a call to that function.

Using functions makes your programs easier to read, and good function names summarize what each part of a program does. Reading a series of function calls gives you a much quicker sense of what a program does than reading a long series of code blocks.

Functions also make your code easier to test and debug. When the bulk of your program’s work is done by a set of functions, each of which has a specific job, it’s much easier to test and maintain the code you’ve written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.