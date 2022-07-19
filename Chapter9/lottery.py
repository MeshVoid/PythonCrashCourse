# Exercise 9-14. From the book Python Crash Course 2nd Edition by Erick Matthews

# Lottery: Make a list or tuple containing a series of 10 numbers and five
# letters. Randomly select four numbers or letters from the list and print
# a message saying that any ticket matching these four numbers or letters
# wins a prize.


# Exercise 9-15. From the book Python Crash Course 2nd Edition by Erick Matthews
# Lottery Analysis: You can use a loop to see how hard it might be to win the
# kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give 
# you a winning ticket.

from random import choice

class Lottery:
    
    """Returns a randomly generated """

    def __init__(self, letters_numbers=None):
        self.letters_numbers = ['a', 'b', 'c', 'd',
                                'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.my_ticket = []
        self.winning_tickets = []
    
    def intro(self):
        """Prints an introduciton text"""
        print("Welcome to the lottery!")

    def select_ticket(self, num_of_tickets):
        """Pick random letters and numbers from the list and return a ticket number"""
        numbers = [num for num in self.letters_numbers if isinstance(num, (int))] # choose only numbers from the list
        letters = [lttr for lttr in self.letters_numbers if isinstance(lttr, str)] # choose only letters from the list
        for i in range(num_of_tickets):
            print(f"Ticket {choice(numbers)}{choice(letters)} wins the lottery!")

    def my_ticket(self):
        """Returns the number of times it took to win the lottery"""
        pass


lottery = Lottery()
lottery.intro()
lottery.select_ticket(5)