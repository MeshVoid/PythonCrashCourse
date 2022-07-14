def send_messages(messages, sent_messages):
    '''Print a text message from the list and removes it while adding to another list'''
    while messages:
        removed_message = messages.pop()
        print(f"Message sent: {removed_message}")
        sent_messages.append(removed_message)