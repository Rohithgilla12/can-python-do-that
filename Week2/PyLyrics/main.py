from PyLyrics import *

albums = PyLyrics.getAlbums(singer='Eminem')
for a in albums:
    print(a)

print(PyLyrics.getLyrics('Eminem', 'Venom'))
