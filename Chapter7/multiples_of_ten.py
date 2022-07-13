# Exercise 7-3. From the book Python Crash Course 2nd Edition by Erick Matthews
# Multiples of Ten: Ask the user for a number, and then report whether the number
#  is a multiple of 10 or not.

print("Just tell me the number and I will tell you if the number is a multiple of 10 or not.")
number = input()

if int(number) % 10 == 0:
    print("It's a multiple of ten!")
else:
    print("It's not a multiple of ten!")
