# Exercise 6-3. From the book Python Crash Course 2nd Edition by Erick Matthews
# 
# A Python dictionary can be used to model an actual dictionary. However, 
# to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.

# • Print each word and its meaning as neatly formatted output. You might print 
# the word followed by a colon and then its meaning, or print the word on one line 
# and then print its meaning indented on a second line. Use the newline character 
# (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'string': 'arrays of bytes representing unicode characters',
    'list': 'mutable, changeable, ordered sequence of elements',
    'variable': 'a symbolic name/reference or pointer to an object',
    'if statement': 'statement evaluating whether a condition is equal to true or false',
    'else': 'if previous conditions were False, try this condition',
    'integer': 'whole number, positive or negative without decimals',
    'float': 'floating-point number that is not an integer',
}

for word in glossary:
    print(f"\n{word.title()}: {glossary[word]}")

