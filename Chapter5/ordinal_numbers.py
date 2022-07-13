# Exercise 5-11. From the book Python Crash Course 2nd Edition by Erick Matthews

# Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
# Most ordinal numbers end in th, except 1, 2, and 3.
#------------------------------------------------------------------------------------------
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal end-ing for each 
# number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result 
# should be on a separate line.
#------------------------------------------------------------------------------------------


numbers = "1 2 3 4 5 6 7 8 9".split()

for number in numbers:
    if number == "1":
        print("1st")
    elif number == "2":
        print("2nd")
    elif number == "3":
        print("3rd")
    else:
        print(f"{number}th")