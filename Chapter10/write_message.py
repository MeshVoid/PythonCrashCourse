filename ='Chapter10\programming.txt' # file adress

with open(filename, 'w') as file_object: # we use second argument 'w' to open the file in WRITE MODE.
    file_object.write("I love programming.\n") # use write() method on the file object to write a string to the file.
    file_object.write('I love creating new games.\n')