def count_words(file_name):
    """Count the approximate number of words in a file"""
    try:
        with open(file_name, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ['Chapter10/alice.txt', 'Chapter10/guest_book.txt', 'siddhartha.txt']
for file_name in file_names:
    count_words(file_name)

