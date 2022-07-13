# Counting_to_twenty.py

# Exercise 4-4. From the book Python Crash Course 2nd Edition by Erick Matthews

# One Million: Make a list of the numbers from one to one million, and then use 
# a for loop to print the numbers. (If the output is taking too long, stop it by 
# pressing Ctrl-C or by closing the output window.)

numbers = []
for i in range(1,1000_001):
    numbers.append(i)
print(numbers[-1])

numbers = []
numbers = [i for i in range(1, 1000_001)]
print(numbers[-1])

# Exercise 4-5. From the book Python Crash Course 2nd Edition by Erick Matthews

# Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and 
# ends at one million. Also, use the sum() function to see how quickly Python 
# can add a million numbers.
numbers = []
numbers = [i for i in range(1, 1000_001)]
print(f"\nMaximum number in the list: {max(numbers)}, Minimum number in the list:{min(numbers)}")
print(f"Sum of all entries in the list: {sum(numbers)}.")
