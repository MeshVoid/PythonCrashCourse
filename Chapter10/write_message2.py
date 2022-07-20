filename = 'Chapter10\programming.txt'

with open(filename, 'a') as file_object: # 'a' argument to open the file for appending rather writing over the existing file.
    file_object.write("\nI also love finding meaning in large datasets.\n") # write two new lines, which are added to programming.txt
    file_object.write("I love creatig apps that can run in a browser.\n")