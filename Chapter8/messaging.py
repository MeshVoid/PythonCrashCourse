# Exercise 8-16. From the book Python Crash Course 2nd Edition by Erick Matthews
# Imports: Using a program you wrote that has one function in it, store that function
# in a separate file. 
# 
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# imports should be up, according to the styling guide, I know that, it's just an exercise ffs.

import message_module

messages_to_send = ["howdie!", "hope you are doing fine!", "Hope I don't die writing my game"]
messages_sent = []

message_module.send_messages(messages_to_send, messages_sent)

from message_module import send_messages as sm

sm(messages_to_send,messages_sent)

import message_module as msgm

msgm.send_messages(messages_to_send, messages_sent)

from message_module import *

message_module.send_messages(messages_to_send, messages_sent)
