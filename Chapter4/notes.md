# CHAPTER 4
## Working with lists

Looping allows you to take the same action, or set of actions, with every item in a list. As a result, you’ll be able to work efficiently with lists of any length, including those with thousands or even millions of items.

**Use a for loop to print out each name in a list:**

```python
magicians = ['alice','david','carolina']****
for magician in magicians:
    print(magician)
```

_It is helpful to choose a meaningful variable name that represents a single item from the list._

For example:
> for **cat** in cats:
> 
> for **dog** in dogs:
> 
> for **item** in list_of_items:

Such naming conventions can help you follow the action being done on each item within a for loop. Using singular
and pluar names can help you identify whether a section of code is working with a single element from the list or 
the entire list.

## Doing more work within a for loop

```python
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```
Make sure to use those indentations to keep the code in the loop, boy.

## Doing something after a for loop

Any lines of code after the for loop that are not indented are executed once without repetition. 

```python
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

print("\n")
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("\nThank you,everyone. That was a great magic show!")

```

# Making numerical lists

Lists are ideal for storing sets of numbers, and Python provides a variety of tools to help you work
efficiently with lists of numbers. Once you undestand how to use these tools effectively, your code 
will work well even when your lists contain millions of items.

## Using the range() function

Python's _range()_ function makes it easy to generate a series of numbers. For example, you can use the
_range()_ function to print a series of numbers:

```python
for value in range(1, 5):
    print(value)
```

In this example, range() prints only the numbers 1 through 4. This is another result of the off-by-one behavior you’ll see often in programming languages. The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.

You can also pass _range()_ only one argument, and it will start the sequence of numbers at 0. For example, range(6)
would return the numbers from 0 through 5.


## Using range() to Make a List of Numbers

If you want to make a list of numbers, you can convert the results of range()directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.

```python
numbers = list(range(1, 6))
print(numbers)
```

We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

```python
even_number = list(range(2,11,2))
print(even_number)
```

You can create almost any set of numbers you want to using the range()function. For example, consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents. Here’s how you might put the first 10 square numbers into a list:

```python
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
```
or: 

```python
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
```

## Simple Statistics with a list of numbers

A few Python function are helpful when working with lists of numbers. For example, you can easily find the 
minimum, maximum, and sum of a list of numbers using _**min(), max(), sum()**_ functions

```python
digits = [1,2,3,4,5,6,7,8,9,0]

min(digits)
max(digits)
sum(digits)
```

## List Comprehensions

The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. 

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

# Working with a part of a list

## Slicing a list

To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function,
Python stops one item before the soceond index you specify. To output the first three elements in a list, you would request
indices  0 through 3, which would return elements 0, 1, and 2.

```python
players = ['charles','martina','michael','florence','eli']

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

```


## Looping through a slice

You can use a slice in a for loop if you awnt to loop through a subset of elements in a list.

```python
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
```

# Copying a List

Often, you’ll want to start with an existing list and make an entirely new list based on the first one. 
Let’s explore how copying a list works and examine one situation in which copying a list is useful.

_To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list._

```python
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] 
# this tells python to make a slice that starts at the first 
# and ends with the last item, making a copy of the list


# Copying the value without slicing won't create a separate list:
# THIS WON'T WORK!
# friend_foods = my_foods

my_foods.append('ravioli')
friend_foods.append('beshparmak')

print ('My favourite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

Important that if you just use = sign, without [:] slicing, then you won't make a unique copy of the list


# TUPLES

Lists work well for storing collections of items that can change troughout the life of a program. 
However, sometimes you might want to create a list of items that cannot changes.
_**Tuples**_ allow you to do just that. 

Python refers to values that cannot change as immutable, and an immutable list is called a _tuple_.

## Defining a tuple

A tuple looks just like a list except you use parenthesis instead of square brackets -> ().
Once you define a tuple, you can access individual elements by using each item's index, just as
you would for a list.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This will cause error, because tuples are immutable:
# dimensions[0] = 250
```

_If you want to define a tuple with a single element, you need to include a trailing comma:_

```python
my_t = (3,)
```

## Looping through all values in a tuple

```python
for dimension in dimensions:
    print(dimension)

```

_Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple._

```python
dimensions = (200, 50)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)



dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```

Python doesn’t raise any errors when we do it, because reassigning a variable is valid. When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed through-out the life of a program.


# STYLING YOUR CODE

Python programmers have agreed on a number of styling conven-tions to ensure that everyone’s code is structured in roughly the same way. Once you’ve learned to write clean Python code, you should be able to understand the overall structure of anyone else’s Python code, as long as they follow the same guidelines.

The guidelines are called PEP (Python Enhancement Proposal).

The Python style guide was written with the understanding that code is read more often than it is written. You’ll write your code once and then start reading it as you begin debugging. When you add features to a pro-gram, you’ll spend more time reading your code. When you share your code with other programmers, they’ll read your code as well.

##  Indentation

PEP 8 recommends that you use four spaces per indentation level. Using four spaces improves readability while leaving room for multiple levels of indentation on each line.In a word processing document, people often use tabs rather than spaces to indent. This works well for word processing documents, but the Python interpreter gets confused when tabs are mixed with spaces. Every text editor provides a setting that lets you use the TaB key but then converts each tab to a set number of spaces. You should definitely use your TaB key, but also make sure your editor is set to insert spaces rather than tabs into your document.Mixing tabs and spaces in your file can cause problems that are very difficult to diagnose. If you think you have a mix of tabs and spaces, you can convert all tabs in a file to spaces in most editors.

## Line Length

Many Python programmers recommend that each line should be less than 80 characters. Historically, this guideline developed because most com-puters could fit only 79 characters on a single line in a terminal window. Currently, people can fit much longer lines on their screens, but other rea-sons exist to adhere to the 79-character standard line length. Professional programmers often have several files open on the same screen, and using the standard line length allows them to see entire lines in two or three files that are open side by side onscreen. PEP 8 also recommends that you limit all of your comments to 72 characters per line, because some of the tools that generate automatic documentation for larger projects add formatting characters at the beginning of each commented line.

The PEP 8 guidelines for line length are not set in stone, and some teams prefer a 99-character limit. Don’t worry too much about line length in your code as you’re learning, but be aware that people who are work-ing collaboratively almost always follow the PEP 8 guidelines. Most editors allow you to set up a visual cue, usually a vertical line on your screen, that shows you where these limits are.

# Blank Lines

To group parts of your program visually, use blank lines. You should use blank lines to organize your files, but don’t do so excessively. 