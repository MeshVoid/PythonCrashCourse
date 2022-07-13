# Exercise 8-3. From the book Python Crash Course 2nd Edition by Erick Matthews

# T-Shirt: Write a function called make_shirt() that accepts a size and the text
#  of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(size, text='placeholder text'):
    print("\nMaking shirt with following specs:")
    print(f"Size of the shirt: {size}")
    print(f"Text on the shirt: {text}")


make_shirt('Medium', "I'm with stupid")

make_shirt(text="Too fat to fail", size="Large")


# Exercise 8-4. From the book Python Crash Course 2nd Edition by Erick Matthews

# Large Shirts: Modify the make_shirt() function so that shirts are large by
# default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# different message.


def make_shirt(text='I love Python', size='large'):
    print("\nMaking shirt with following specs:")
    print(f"Size of the shirt: {size}")
    print(f"Text on the shirt: {text}")


make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='extra-large', text = "I'm too dumb")