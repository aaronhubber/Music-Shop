from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Radiohead')
artist2 = Artist('Red Hot Chilli Peppers')
artist3 = Artist ('Sam Cooke')

artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)

album1 = Album('OK Computer', 'reggie', artist1)
album2 = Album('Mothers Milk', 'pop-punk', artist2)
album3 = Album('Portrait of a Legend', 'soul', artist3)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)


album1.genre = "indie"
album_repository.update(album1)

for album in album_repository.select_all():
    print (album.__dict__)





