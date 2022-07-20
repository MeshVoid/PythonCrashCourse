# Exercise 10-4. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# Guest Book: Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line
# recording their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.
import datetime

file_name = 'Chapter10\guest_book.txt'

run = True
while run:
    user_name = input("Please input guest's name:\n")
    with open(file_name, 'a') as file_object:
        file_object.write(
            f"Date of visit: {datetime.date.today()}. Guest name:{user_name.title()} \n")
    new_guests = input("Do you wish to add new guest entry? y/n \n")
    if new_guests.lower()[0] == 'y':
        run = True
    else:
        print(f"Alright! All entries can be found here:")
        print(f"\t{file_name}")
        run = False
        break
