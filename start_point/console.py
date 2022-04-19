from models.artist import Artist
import respositories.artist_repository as artist_repository

artist1 = Artist('Radiohead')
artist2 = Artist('Red Hot Chilli Peppers')
artist3 = Artist ('Same Cooke')

artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)