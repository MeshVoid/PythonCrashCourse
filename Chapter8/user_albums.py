# Exercise 8-8. From the book Python Crash Course 2nd Edition by Erick Matthews

# User Albums: Start with your program from Exercise 8-7. Write a whileloop that
# allows users to enter an album’s artist and title. Once you have that information,
# call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.




def make_album(artist_name='', album_title='', num_songs = None):
    album = {'artist': artist_name, 'album title': album_title}
    if num_songs:
        album['number of songs'] = num_songs
    return album

polling = True

while polling:
    artist_name = input("Enter artist's name: ")
    album_title = input("Enter Album's title: ")
    num_songs = input("Enter number of songs:")
    album = make_album(artist_name, album_title, num_songs)
    ask_quit = input("Input quit or q to quit ")
    if 'q' in ask_quit or 'quit' in ask_quit:
        polling = False

print(album)

