- _Variable names can contain only letters, numbers, and underscores._
- _Variables can start with a letter or an underscor, but not wih a number_
- _Spaces are not allowed in variable names, but underscores can be used to separate words_
- _Variable names should be short but descriptive_ 
- _Be careful when using lowercase letter l and the uppercase letter 0, as they can be_
  _confused with the numbers 1 and 0._


# Strings
String - is a series of characters. Anything inside quotes is considered a string in Python, and you can use
single or double quotes around your strings like this:
"This is a string."
'This is also a string.'

-String Methods:
method _title()_ - changes each word to title case, where each word begins with a capital letter.

F-Strings
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# strings like these are called f-strings. f stands for format. we use them to inser variables into a string
print(full_name)
```

To add tab use \t
Example:
```python
print("\tPython")
```
To add a newline in a string, use the character combination \n:
```python
print("Languages:\nPython\nC\nJavaScript")
```

*You can also combine \n\t"
```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

## Stripping Whitespace
**Use rstrip() method to remove whitespaces - FROM THE RIGHT SIDE**
```python
favorite_language = 'python '
favorite_language.rstrip()
```
**Use lstrip() method to remove whitespaces - FROM THE RIGHT SIDE**
```python
favorite_language = 'python '
favorite_language.lstrip()
```
**Use strip() method to remove ALL WHITE SPACES!**
```python
favorite_language = 'python '
favorite_language.strip()
```

## Avoiding Syntax Errors with Strings
-Use double quotes to avoid apostrophe related errors.
```python
#apostrophe.py 
# Avoiding Syntax Errors with Strings
message = "One of Python's strenths is its diverse community."
#doublequotes to apustrophe
print(message)
```

# NUMBERS IN PYTHON

## INTEGERS

_You can use + , - , * , / with integers to add, subtract, multiply, and divide_
```python
2 + 3
3 - 2
2 * 3
3 / 2
```

_Python uses two multiplication symbols to represent exponents_
```python
3 ** 2
3 ** 3
10 * 6
```
_Python also supports the order of operations too:_
```python
>- For example:
>  2 + 3 * 4 # will result to 14
>  (2 + 3) * 4 # will result in 20, as brackets take precedence
```

# FLOAT NUMBERS
```python
0.1 + 0.1
0.2 + 0.2
# and etc.
```

## INTEGERS AND FLOATS

> input: 4/2 # when you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float value!
> output: 2.0

_If you mix an integer and a float in any other operation, you'll get a float as well:

```python
1 + 2.0 # result: 3.0
2 * 3.0 # result: 6.0
```
Python defaults to a float in any operation that uses a float, even if the output is a whole number

## Underscores in Numbers

_When you are writing numbers, you can group digits using underscores to make large numbers more readable_

```python
universe_age = 14_000_000_000
print(universe_age)
14000000000
```
Python ignores underscores for both float and int values



## MULTIPLE ASSIGNMENT

You can assign values to more than one variable using a single line of code in Python:
```python
x, y, z = 0, 0, 0
```

# CONSTANTS

_**Constant - is a variable whose value stays the same throughout the life of a program.
Python doesn't have built-in constant types, but Python programmers use all capital letters
to indicate a variable shouls be treated as a constant and never be changed.**_
```python
MAX_CONNECTIONS = 5000
```

# COMMENTS
```python
# - indicates a comment

''' this is a 
multiline comment '''
```
# ZEN OF PYTHON

Experienced Python programmers will encourage you to avoid complexity and aim for simplicity
whenever possible. The Python community's philosophy is contained in "The Zen of Python" 
by Tim Peters. To read the brief set of principles use:

```python
import this
```

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!