# Exercise 10-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents
# of the file to the screen. Wrap your code in a try-except block to catch the
# FileNotFound error, and print a friendly message if a file is missing. Move
# one of the files to a dif-ferent location on your system, and make sure the
# code in the except block executes properly.

def read_files(file_name):
    try:
        with open(file_name, encoding = "utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"\nSorry, but the file {file_name} not found.")
    else:
        print(f"\nContents of a {file_name} file:\n{contents}")

file_names = ["Chapter10/dogs.txt", "Chapter10/cats.txt", "dicks.txt"]

for file_name in file_names:
    read_files(file_name)