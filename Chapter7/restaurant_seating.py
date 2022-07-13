# Exercise 7-2. From the book Python Crash Course 2nd Edition by Erick Matthews

# Restaurant Seating: Write a program that asks the user how many people are in 
# their dinner group. If the answer is more than eight, print a message saying 
# they’ll have to wait for a table. Otherwise, report that their table is ready.

print("Hello there welcome to our restaurant!")
number_of_people = input("Can you tell me how many people in your dinner group? ")

if int(number_of_people) > 8:
    print("Sorry all seats are taken, you will have to wait for a table.")
else:
    print("Splendid! We just have a right place for you and your company!")