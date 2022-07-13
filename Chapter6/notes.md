# Chapter 6
# Dictionaries

Dictionaries in Python allow you to connect pieces of related information. Understanding
dictionaries allows programmer to model a variety of real-world objects more accurately.

In a dictionary you can store two kinds of information that can be matched up, such as
a list of words and their meanings.

## A simple dictionary

A simple dictionary can look like this:

```python
#alien.py
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) # green
print(alien_0['points']) # 5
```

## Working with dictionaries

A dictionary in Python is collection of key-value pairs. Each key is connected to a value,
and you use a key to access the value associated with that key. 

**_A key's value can be a number, a string, a list, or even another dictionary. In Python you can use ANY object that you can create as a value in a dictionary._**

A dictionary is wrapped in braces **{}**, with a series of key-value pairs inside the braces:
```python
alien_0 = {'color': 'green', 'points': 5}
```

Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
You can store as many key-value pairs as you want in a dictionary.

The simplest form of a dictionary has only ONE key-value pair:
```python
alien_0 = {'color': 'green'}
```

## Accessing values in a dictionary

To get the value associated with a key, give the name of the dictionary and then place the key inside
a set of square brackets:

```python
alien_0 = {'color':'green'}
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```

## Adding new key-value pairs

Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
For example, to add a new key-value pair, you would give the name of the dictionary followed by the
new key in square brackets along with the new value.

```python
alien_0 = {'color': 'green', 'points': 5}

# addling new key-values to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

## Starting with an empty dictionary

It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each
new item to it. To start filling an empty dictionary, define a dictionary with an empty set of 
braces and then add each key-value pair on its own line.

```python
alien_0 = {} # defining an empty dictionary

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```

Typically you will use empty dictionaries when you would like to store data supplied by a user
in a dictionary or when you would like to write code that will generate a large number of key-value
pairs automatically.

## Modifying valued in a dictionary

To modify a value in a dictionary you type in the name of the dictionary with the key in square brackets
and then the new value you want to be associated with that key.

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
```

Modifying dictionary with if-elif-else chain:

```python
alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
```

## Removing key-value pairs

When you no longer need a piece of information that's stored in a dictionary, you can use
the _**del**_ statement to delete it completely.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

_Be aware that the deleted key-value pair is removed permanently._

## A dictionary of similar objects

You can also use a dictionary to store one kind of information about many objects.
For example, you want to poll a number of people and ask them what their favorite
programming language is.

A dictionary to store such a poll would look like this:
```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
```

## Using get() to access values

Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.
```python
alien_0 = {'color': 'green'}
print(alien_0['points']) # will cause a KeyError message
```
To avoid getting an error use the _**get()**_ method to set a default value that will be returnde if the requested key doesn't
exist in the dictionary.

The _**get()**_ method requires a key as a first argument. As a second optional argument, you can pass the value to be returned
if the key doesn't exist:

```python
print('\n')

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```

In the example above if the key 'points' exists in the dictionary, you'll get the corresponding value. If it doesn't, you get the
default value. In this case, it wil print: "No point value assigned." instead of rendering an error.'

**! Remember that if there's a chance that the key you're looking for in the dictionary might not be there, consider using the 
get() methoc instead of the square bracket notation.**

# Looping through a dictionary

A single Python dictionary can contain just a few key-value pairs or millions of pairs. Python lets you loop through a dictionary.

There are several different ways to loop through dictionaries. You can loop through whole dictionary's key-value pairs,
only through its keys, or through it's values.

## Looping through all key-value pairs.

You could loop through the dictionary using a for loop:

```python
# user.py
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items(): # we use method items() and key, value to loop through the whole dictionary
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

Another example:

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
```

## Looping through all the keys in a dictionary

The _**keys()**_ method is useful when you don't need to work with all of the values in a dictionary.

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name in favourite_languages.keys():
    print(name.title())
```

_Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you did this:_

```python
for name in favourite_languages:
```
rather than:

```python
for name in favourite_languages.keys():
```

You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

You can access the value associated with any key you care about inside the loop by using the current key.

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```

## Looping through a dictionary's keys in a particular order

Starting in Python 3.7, looping through a dictionary returns the items in the same order they were inserted. 
One way to do this is to sort the keys as they’re returned in the for loop. 

You can use the sorted() function to get a copy of the keys in order:

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

## Looping through all values in a dictionary

If you are interested only in values that dictionary contains, use the _**values()**_ method to return a list
of values without any keys.

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())
```

This approach pulls all the values from the dictionary but in a dictionary with a large number of repetitions,
this method might not be preferrable. You can use sets to avoid repetitions.

_**Set**_ - collection in which each item must be unique:

```python
favourite_languages ={
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("\nThe following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
```

When we wrap set() method around a list that contains duplicate items, Python identifies the unique items in the list
and builds a set from those items.

# SETS

You can build sets using {} and separating the elements with commas:
```python
languages = {'python','ruby','python','c'}
languages # {'ruby','python','c'}
```

# Nesting

If you want to store multiple dictionaries in a list, or a list of items as a value in a dictionary you will use **_nesting_**.

You can **nest** dictionaries inside a list, a list of items inside a dictionary, dictionary inside another dictionary.

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # nesting multiple dictionaries into one list

print(aliens)

for alien in aliens:
    print(alien)
```

Another example that uses range() to create 30 alien dictionaries in the list:

```python
aliens = []
# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
```

We can use a for loop and if statement to make changes to such lists:

```python
print('\n')

aliens = []
# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
```
We could expand this block with elif statement

```python
aliens = []
# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15      

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
```

## A list in a dictionary

Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary. 

Example:
```python
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)****
```

Another example of nesting a list inside a dictionary:

```python
{
favourite_languages ={
    'jen ':['python','ruby'],
    'sarah':['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python','haskell']
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
}
```

Try not to **overuse nesting** because you then might get confused at the code.

## A Dictionary in a dictionary

You can nest a dictionary inside another dictionary, but then your code will get complicated very quickly.

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

Notice how in the example above the structure of users dictionary is identical. Althought 
following structure is not required by Python, identical structure of the keys and values
when nesting a dictionary inside a dictionary makes it easier to fork with and use for loops.