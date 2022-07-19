filename = 'Chapter10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


pi_string = '' # create a varible to hold the digits of pi
for line in lines: # create a loop to add each line of digits to pi_string
    pi_string += line.rstrip() # and remove character from each line

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")