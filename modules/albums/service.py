from modules.albums.use_cases.get_album_by_id import GetAlbumByIdUseCase
from modules.albums.use_cases.get_album_by_link import GetAlbumByLinkUseCase

class AlbumService:
    def __init__(self):
        self.get_album_by_id_use_case = GetAlbumByIdUseCase()
        self.get_album_by_link_use_case = GetAlbumByLinkUseCase()

    def get_album_by_id(self, album_id: str):
        return self.get_album_by_id_use_case.execute(album_id)

    def get_album_by_link(self, token: str):
        return self.get_album_by_link_use_case.execute(token)
