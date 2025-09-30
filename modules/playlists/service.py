from modules.playlists.use_cases.get_playlist_by_id import GetPlaylistByIdUseCase
from modules.playlists.use_cases.get_playlist_by_link import GetPlaylistByLinkUseCase

class PlaylistService:
    def __init__(self):
        self.get_playlist_by_id_use_case = GetPlaylistByIdUseCase()
        self.get_playlist_by_link_use_case = GetPlaylistByLinkUseCase()

    def get_playlist_by_id(self, playlist_id: str, limit: int, page: int):
        return self.get_playlist_by_id_use_case.execute(playlist_id, limit, page)

    def get_playlist_by_link(self, token: str, limit: int, page: int):
        return self.get_playlist_by_link_use_case.execute(token, limit, page)
