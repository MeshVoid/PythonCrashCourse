# Exercise 8-10. From the book Python Crash Course 2nd Edition by Erick Matthews

# Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
# that prints each text message and moves each message to a new list called sent_messages as 
# it’s printed. After calling the function, print both of your lists to make sure the messages 
# were moved correctly.

messages = ['hello world!', 
            'this is a short message', 
            'I hope the world will not end till I finish this book']

sent_messages = []

def send_messages(messages, sent_messages):
    '''Print a text message from the list and removes it while adding to another list'''
    while messages:
        removed_message = messages.pop()
        print(f"Message sent: {removed_message}")
        sent_messages.append(removed_message)

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)