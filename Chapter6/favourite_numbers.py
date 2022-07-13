# Exercise 6-2. From the book Python Crash Course 2nd Edition by Erick Matthews

# Favorite Numbers: Use a dictionary to store people’s favourite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a 
# favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

favourite_numbers = {
    'Steve':'12',
    'Lucy':'13',
    'Aigerim':'666',
    'Rafael':'13',
    'Maksat':'12'
}

for numbers in favourite_numbers:
    print(f"{numbers}'s favourite number: {favourite_numbers[numbers]}")