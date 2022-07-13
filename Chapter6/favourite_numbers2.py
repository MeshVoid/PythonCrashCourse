# Exercise 6-10. From the book Python Crash Course 2nd Edition by Erick Matthews

# Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person
# can have more than one favorite number. Then print each person’s name along
# with their favorite numbers.


favourite_numbers = {
    'Steve': [12, 13, 56],
    'Lucy': [14, 22, 67],
    'Aigerim': [666, 6],
    'Rafael': [0, 4, 33],
    'Maksat': [8, 777, 98]
}

for names, numbers in favourite_numbers.items():
    print(f"\n{names}'s favourite numbers are:")
    for i in numbers:
        print(f"\t{i}")