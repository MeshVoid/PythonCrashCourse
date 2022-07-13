# Exercise 4-7. From the book Python Crash Course 2nd Edition by Erick Matthews

# Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

threes = []
for i in range(3, 30, 3):
    threes.append(i)
    print(threes)