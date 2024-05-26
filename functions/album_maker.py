# Dylan Nelson
# April 02, 2024
# album_maker.py

# Function that builds a dictionary 
def make_album(artist_name, album_title, n_of_songs = 7):
    '''Creates an album with the name of the artist, album and the number of 
    songs'''
    album = {
        'name': artist_name,
        'title': album_title,
        'number of songs': n_of_songs, 
    }
    return album

my_album = make_album(
    artist_name='dance', 
    album_title='green sandpit paradise', 
    n_of_songs= 3,
    )
print(my_album)

# This is a while loop that will ask the user to enter an artists name
# and album title and number of songs
while True:
    print('Type q at any time to quit.')
    artist_name = input('What is the name of the artist? ')
    if artist_name == 'q':
        break
    album_title = input('What is the album title? ')
    if album_title == 'q':
        break
    n_of_songs = input('How many songs are there in the album? ')
    if n_of_songs == 'q':
        break
    my_album = make_album(artist_name, album_title, n_of_songs)
    print(my_album)