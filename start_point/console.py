from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist1 = Artist('Radiohead')
artist2 = Artist('Red Hot Chilli Peppers')
artist3 = Artist ('Sam Cooke')

artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)

album1 = Album('OK Computer', 'indie', artist1)
album2 = Album('Mothers Milk', 'pop-punk', artist2)
album3 = Album('Portrait of a Legend', 'soul', artist3)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)

album_repository.delete(album2)



