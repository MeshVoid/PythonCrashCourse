'''message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# let's make this program run until user quits using while loop

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != 'quit':
        print(message)



'''

# using a flag in a while statement

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

