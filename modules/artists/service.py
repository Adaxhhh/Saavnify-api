from modules.artists.use_cases.get_artist_by_id import GetArtistByIdUseCase
from modules.artists.use_cases.get_artist_by_link import GetArtistByLinkUseCase
from modules.artists.use_cases.get_artist_songs import GetArtistSongsUseCase
from modules.artists.use_cases.get_artist_albums import GetArtistAlbumsUseCase

class ArtistService:
    def __init__(self):
        self.get_artist_by_id_use_case = GetArtistByIdUseCase()
        self.get_artist_by_link_use_case = GetArtistByLinkUseCase()
        self.get_artist_songs_use_case = GetArtistSongsUseCase()
        self.get_artist_albums_use_case = GetArtistAlbumsUseCase()

    def get_artist_by_id(self, artist_id: str, page: int, song_count: int, album_count: int, sort_by: str, sort_order: str):
        return self.get_artist_by_id_use_case.execute(artist_id, page, song_count, album_count, sort_by, sort_order)

    def get_artist_by_link(self, token: str, page: int, song_count: int, album_count: int, sort_by: str, sort_order: str):
        return self.get_artist_by_link_use_case.execute(token, page, song_count, album_count, sort_by, sort_order)

    def get_artist_songs(self, artist_id: str, page: int, sort_by: str, sort_order: str):
        return self.get_artist_songs_use_case.execute(artist_id, page, sort_by, sort_order)

    def get_artist_albums(self, artist_id: str, page: int, sort_by: str, sort_order: str):
        return self.get_artist_albums_use_case.execute(artist_id, page, sort_by, sort_order)
