from modules.songs.use_cases.get_song_by_id import GetSongByIdUseCase
from modules.songs.use_cases.get_song_by_link import GetSongByLinkUseCase
from modules.songs.use_cases.get_song_suggestions import GetSongSuggestionsUseCase

class SongService:
    def __init__(self):
        self.get_song_by_id_use_case = GetSongByIdUseCase()
        self.get_song_by_link_use_case = GetSongByLinkUseCase()
        self.get_song_suggestions_use_case = GetSongSuggestionsUseCase()

    def get_song_by_ids(self, song_ids: str):
        return self.get_song_by_id_use_case.execute(song_ids)

    def get_song_by_link(self, token: str):
        return self.get_song_by_link_use_case.execute(token)

    def get_song_suggestions(self, song_id: str, limit: int):
        return self.get_song_suggestions_use_case.execute(song_id, limit)
