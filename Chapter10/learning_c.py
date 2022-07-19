# Exercise 10-2. From the book Python Crash Course 2nd Edition by Erick Matthews
#
# Learning C: You can use the replace() method to replace any word in a string
# with a different word. Here’s a quick example showing how to replace 'dog'
# with 'cat' in a sentence:

# >>>message = "I realy like dogs."
# message.replace('dog','cat')

# Read in each line from the file you just created, learning_python.txt, 
# and replace the word Python with the name of another language, such as C. 
# Print each modified line to the screen.

file_name = 'Chapter10\learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        #print(line.rstrip())
        print(line.rstrip().replace('Python', 'C'))