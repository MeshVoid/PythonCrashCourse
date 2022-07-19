# Exercise 10-1. From the book Python Crash Course 2nd Edition by Erick Matthews

# Learning Python: Open a blank file in your text editor and write a few lines
# summarizing what you’ve learned about Python so far. Start each line with the
# phrase In Python you can...
# 
# Save the file as learning_python.txt in the same directory as your exercises
# from this chapter. Write a program that reads the file and prints what you
# wrote three times. Print the contents once by reading in the entire file,
# once by looping over the file object, and once by storing the lines in a
# list and then working with them outside the with block.

file_name = 'Chapter10\learning_python.txt'

with open(file_name) as file_object:
    #contents = file_object.read()
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


#print(contents)
#print(lines)

for line in lines:
    print(line.rstrip())