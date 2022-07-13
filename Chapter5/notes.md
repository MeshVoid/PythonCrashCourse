# If else statements

- Programming often involves examining a set of conditions and deciding which action to take based on those conditions.
  Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.

## A simple example

Imagine you have a list of cars and you want to print out the name of each car. Car names are proper names,
so the names of most cars should be printed in title case. However, the value 'bmw' should be printed in all
uppercase. The following code loops through a list of car names and looks for the value 'bmw'.
Whenever the value is 'bmw', it’s printed in uppercase instead of title case:

```python
# cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

## Conditional tests

At the heart of every if statement is an expression that can be evaluated as _True_ or _False_ and is called
a conditional test.
We tell Python with our code that if the condition is _True_ the we execute the code following the if statement.
If the codition is _False_ then Python will ignore the code following the if statement block.

## Checking for Equality

Most conditional tests compare the current value of a variable to a specific value of interest.

```python
car = 'bmw'
car == 'bmw' # this line will return True
```

_(==) equality operator_ returns **True** or **False** if the values on the left
and right side of the operator match or don't.

Testing for equality is case sensitive in Python:

```python
car = 'Audi'
car == 'audi' # will return False
```

You can covert the varaible's value to lowercase before doing the comparison:

```python
car = 'Audi'
car.lower() = 'audi' # will return True
```

## Checking for Inequality

When you want to determine whether two values are not equal, you can combine
an exclamation point and an equal sign (!=). The exclamation point represents
_not_, as it does in many programming languages.

How to use it:

```python
# toppings.py
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

_Most of the conditional expressions you write will test for equality, but sometimes you’ll find it more efficient to test for inequality._

# Numerical Comparisons

Comparing numerica values done by ==

Example:

```python
age = 92
age == 92 # this will return True
```

You can also see if two number are not equal:

```python
#magic_number.py
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
```

**You can also include mathematical comparisons:**

```python
age = 19
age < 21 # True
age <=21 # True
age > 21 # False
age >= 21 # False
```

All these comparisons can be and should be used as a part of an **_if statement_**.

# Checking Multiple Conditions

Sometimes you would want to check multiple conditions at the same time. For example,
sometimes you might need two conditions to be **True** to take an action. Other times
you might be satisfied with just one condition being **True**.

## Using **_and_** to check multiple conditions

To check whether two conditions are both **True** simultaneously, use the key-word **_and_** :

```python
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # False

age_1 = 22
age_0 >= 21 and age_1 >= 21 # True
```

To improve readability you can use parentheses areound the individual tests, but are not obliged to do so.
Example:

```python
(age_0 >= 21) and (age_1 >= 21)
```

## Using **_or_** to check multiple conditions

The keyword **_or_** allows you to check multiple conditions as well, but it passes when either or both of the
individual tests pas. An **_or_** expression fails only when both individual tests fail.

Example:

```python
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21 # True

age_0 = 18
age_0 >= 21 or age_1 >= 21 # False
```

# Checking whether a value is in a list

Sometimes you would want to check whether a list contains a certain value before proceeding. To find out whether
a particular value is already in a list, use the keyword **_in_**.

```python
requested_toppings = ['mushrooms', 'onions','pineapple']
'mushrooms' in requested_toppings # True
'pepperoni' in requested_toppings # False
```

# Checking whether a value is **not** in a list

Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation. For example, consider a list of users who are banned from commenting in a forum. You can check whether a user has been banned before allowing that person to submit a comment:

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
  print(f"{user.title()}, you can post a response if you wish.")
```

# Boolean expressions

A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

```python
game_active = True
can_edit = False
```

# If statements

When you understand conditional tests, you can start writing if statements. Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test.

## Simple if statements

Form of if statements:

> if conditional_test:
>
>     do something

Code example:

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

Indentation plays the same role in if statements as it did in for loops. All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

You can have as many lines of code as you want in the block follow-ing the if statement.

## If-else statements

Often, you'll want to take one action when a conditional test passes and a different action in all other cases.
If-else statements make it possible.

**_if-else_** block is similar to simple if statement, but the **_else_** statement allows you to define and action
or set of actions that are executed when the conditional test fails.

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

## The if-elif-else chain

At times you will need to test more than two possible conditions, and to evaluate those you will use Python's
**_if-elif-else_** syntax.

For example, consider an amusement park that charges different rates for different age groups:

- Admission for anyone under age 4 is free.
- Admission for anyone between the ages of 4 and 18 is $25.
- Admission for anyone age 18 or older is $40.

```python
age = 12

if age < 4:
    print("Your admission cost is 0$.")
elif age < 18:
    print("Your admission cost is 25$.")
else:
    print("Your admission cost is 40$.")

# another way to write the program:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is {price}$.")

# It's more efficient less print() statements to edit if needs be

```

# Using Multiple elif blocks

You can use as many elif blocks in your code as you like.

```python
age = 72

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is {price}$.")
```

## Omitting the else block

Python does not require an else block at the end of an if-elif chain. Some-times an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest

```python
age = 74

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >=65:
    price = 20

print(f"Your admission cost is {price}$.")
```

**_If you have a specific final condition you are testing for, consider using a final elif block and omit the else block._**
**_As a result, you'll gain extra confidence that your code will run only under the correct conditions._**

## Testing multiple conditions

The if-elif-else chain is megapowerful, but it's only appropriate to use when you just need one test to pass. As soon as Python
finds one test taht passes, it skips the rest of the tests.
This is very efficient and allows you to test for one specific condition.

However if you need to check multiple conditions, it is simpler to use **_if statements_** with no elif or else blocks.

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes.

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

**_In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements_**

# Using if statements with lists

You can do some interesting work when you combine lists and if statements. You can watch for special values that need
to be treated differently than other values in the list. You can manage changing conditions efficiently. You can use
if statements to check whether your code works as you intended.

## Checking for special items

```python
#toppings.py

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")


print("\nFinished making your pizza!")
```

## Checking that a list is not empty

We can can use if statement to quickly check if a list has any entries and is not empty before running a for loop
or any other piece of code:

```python
requested_toppings = [] #empty list

if requested_toppings: # empty list returns False
    for requested_topping in requested_toppings: # this block will be omitted because the list is empty
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") # this will be printed instead
```

## Using Multiple lists

You can also use if statements with multiple lists. For example we can use two lists to check them
against each other.

Example:
```python
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

## Styling your if statements

The only recommendation PEP 8 provides for styling conditional tests is to use a single
space around comparison operators, such as ==, >=, <=.

for example:
> if age < 4:

is better than:
> if age<4: