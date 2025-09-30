from modules.search.use_cases.search_all.search_all import SearchAllUseCase
from modules.search.use_cases.search_songs.search_songs import SearchSongsUseCase
from modules.search.use_cases.search_albums import SearchAlbumsUseCase
from modules.search.use_cases.search_artists import SearchArtistsUseCase
from modules.search.use_cases.search_playlists import SearchPlaylistsUseCase

class SearchService:
    def __init__(self):
        self.search_all_use_case = SearchAllUseCase()
        self.search_songs_use_case = SearchSongsUseCase()
        self.search_albums_use_case = SearchAlbumsUseCase()
        self.search_artists_use_case = SearchArtistsUseCase()
        self.search_playlists_use_case = SearchPlaylistsUseCase()

    def search_all(self, query: str):
        return self.search_all_use_case.execute(query)

    def search_songs(self, query: str, page: int, limit: int):
        return self.search_songs_use_case.execute(query, page, limit)

    def search_albums(self, query: str, page: int, limit: int):
        return self.search_albums_use_case.execute(query, page, limit)

    def search_artists(self, query: str, page: int, limit: int):
        return self.search_artists_use_case.execute(query, page, limit)

    def search_playlists(self, query: str, page: int, limit: int):
        return self.search_playlists_use_case.execute(query, page, limit)
