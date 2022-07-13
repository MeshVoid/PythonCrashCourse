# Exercise 7-5. From the book Python Crash Course 2nd Edition by Erick Matthews

# Movie Tickets:A movie theater charges different ticket prices depending on a 
# person’s age. If a person is under the age of 3, the ticket is free; if they 
# are between 3 and 12, the ticket is $10; and if they are over age 12, 
# the ticket is $15. Write a loop in which you ask users their age, and then 
# tell them the cost of their movie ticket.

prompt = "\nHello there! What is you age? "
prompt += "Type quit to exit the program >> "


end = False
while end == False:
    user_age = input(prompt)
    if user_age == 'quit':
        end = True
    elif int(user_age) <= 3:
        print("The ticket is free for you kiddo!")
    elif int(user_age) <= 12:
        print("The ticket will cost you 10$!")
    elif int(user_age) > 12:
        print("The ticket will cost you 15$!")