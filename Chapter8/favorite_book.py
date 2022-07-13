# Exercise 8-2. From the book Python Crash Course 2nd Edition by Erick Matthews

# Favorite Book: Write a function called favorite_book() that accepts one parameter,
#  title. The function should print a message, such as One of my favorite books is 
# Alice in Wonderland. Call the function, making sure to include a book title as an 
# argument in the function call.


def favorite_book(book_title):
    print(f"What do you know... My favourite book happens to be: ")
    print(book_title)

favorite_book('Alice in wonderland')