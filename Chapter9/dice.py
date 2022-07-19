# Exercise 9-13. From the book Python Crash Course 2nd Edition by Erick Matthews

# Dice: Make a class Die with one attribute called sides, 
# which has a default value of 6. Write a method called roll_die() 
# that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times.Make a 10-sided die and a 20-sided
# die. Roll each die 10 times.
from random import randint

class Die:
    """A die that rolls the dice"""
    def __init__(self, sides):
        
        self.sides = sides
    
    def roll_die(self, times_to_roll):
        """Roll the dice several times and print the values"""
        print(f"Rolling the dice with {self.sides} sides {times_to_roll} times:")
        for i in range(times_to_roll):
            print(f"\t{randint(0, self.sides)}")



die = Die(6)
die.roll_die(3)
die2 = Die(10)
die2.roll_die(10)
die3 = Die(20)
die3.roll_die(10)

