filename = 'Chapter10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' # create a varible to hold the digits of pi
for line in lines: # create a loop to add each line of digits to pi_string
    pi_string += line.rstrip() # and remove character from each line

print(f"{pi_string[:52]}...") # print the string
print(len(pi_string))