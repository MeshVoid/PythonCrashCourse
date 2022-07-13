# Exercise 8-7. From the book Python Crash Course 2nd Edition by Erick Matthews

# User Albums: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces
# of information.

# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album
# information correctly.
#
# Use None to add an optional parameter to make_album()
# that allows you to store the number of songs on an album. If the calling line
# includes a value for the number of songs, add that value to the album’s
# dictionary. Make at least one new function call that includes the number
# of songs on an album



def make_album(artist_name='', album_title='', num_songs = None):
    album = {'artist': artist_name, 'album title': album_title}
    if num_songs:
        album['number of songs'] = num_songs
    return album

new_album = make_album('Michael Jackson', '10 fists of fury')
print(new_album)
new_album = make_album('Bob Dylan', 'Your dad and I', 32)
print(new_album)
new_album = make_album('Roza Rymbaeva', 'Sladkie utekhi', 168)
print(new_album)
