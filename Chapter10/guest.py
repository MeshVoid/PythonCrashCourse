# Exercise 10-3. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# Guest: Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt.

file_name = 'Chapter10\guest.txt'

user_name = input("Hello there! Please state your name: \n")

with open(file_name, 'a') as file_object:
    file_object.write(f"{user_name.title()} \n")

print(
    f'I have added your name to guestbook. You can find the guestbook file here:\n\t{file_name}')
