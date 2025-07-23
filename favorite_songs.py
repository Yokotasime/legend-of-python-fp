
favorite_songs = {
    'title': 'artist'
}

def write_favorite_songs(favorite_songs, gitkeep):
    file = open('gitkeep.txt', 'w')
    file.write('Im Just Ken - Ryan Gosling' + '\n')
    file.write('I Wanna Be Yours - Arctic Monkeys' + '\n')
    print(f'Songs have been uploaded', end='')
