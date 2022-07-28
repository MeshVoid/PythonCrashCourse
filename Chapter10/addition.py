# Exercise 10-6 and 10-7. From the book Python Crash Course 2nd Edition 
# by Erick Matthews
# 
# Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert the
# input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text
# instead of a number.

# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

def calculator():
    keep_running = True
    while keep_running:
        try:
            number_1 = int(input("Enter the first number: "))
            number_2 = int(input("Enter the second number: "))
        except ValueError:
            print("The value you have entered is not a number, we require a number!")
            continue
        else:
            result = number_1 + number_2
            print(f"The result of adding two numbers you have provided is: ")
            print(f"{result}")
            ask_continue = input("Add another numbers? y/n\n")
            if ask_continue == 'n'.lower():
                keep_running = False
                print("Bye!")
            else: 
                continue

calculator()