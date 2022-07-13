# Exercise 8-9. From the book Python Crash Course 2nd Edition by Erick Matthews

# Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

messages = ['hello world!', 
            'this is a short message', 
            'I hope the world will not end till I finish this book']


def show_messages(any_list):
    '''This function displays a series of short text messages'''
    for message in messages:
        print(f"You message: {message}")

show_messages(messages)