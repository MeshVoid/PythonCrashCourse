# Exercise 6-4. From the book Python Crash Course 2nd Edition by Erick Matthews

# Glossary 2: Now that you know how to loop through a dictionary, clean up the code 
# from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop 
# that runs through the dictionary’s keys and values. When you’re sure that your loop 
# works, add five more Python terms to your glossary. When you run your program again, 
# these new words and meanings should automatically be included in the output.


glossary = {
    'string': 'arrays of bytes representing unicode characters',
    'list': 'mutable, changeable, ordered sequence of elements',
    'variable': 'a symbolic name/reference or pointer to an object',
    'if statement': 'statement evaluating whether a condition is equal to true or false',
    'else': 'if previous conditions were False, try this condition',
    'integer': 'whole number, positive or negative without decimals',
    'float': 'floating-point number that is not an integer',
}

for item in glossary:
    print(f"\n{item.title()}: {glossary[item]}")

# this way is the super simple way with items()
#for item in glossary.items():
    #print(f"\n{item}")