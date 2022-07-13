#stripping_names.py
# Exercise 2-6 Stripping names exercise from the book Python Crash Course 2nd Edition
#
# Use a variable to represent a person’s name, and include some whitespace characters 
# at the beginning and end of the name. Make sure you use each character combination, 
# "\t" and "\n", at least once.

name = " Dick "
print(f"\t{name},\n{name.lstrip()},\n{name.rstrip()},\n{name.strip()}")