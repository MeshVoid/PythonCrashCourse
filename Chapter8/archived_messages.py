# Exercise 8-11. From the book Python Crash Course 2nd Edition by Erick Matthews

# Archived Messages: Start with your work from Exercise 8-10. Call the function 
# send_messages() with a copy of the list of messages. After calling the function,
# print both of your lists to show that the original list has retained its messages.

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

send_messages(messages[:], sent_messages) # using a copy of the list by slicing it [:]

print(messages)
print(sent_messages)