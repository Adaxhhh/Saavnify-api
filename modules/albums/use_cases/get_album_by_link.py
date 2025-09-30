from common.helpers import use_fetch
from modules.albums.helpers import create_album_payload

class GetAlbumByLinkUseCase:
    def execute(self, token: str):
        response = use_fetch('webapi.get', {'token': token, 'type': 'album'})
        
        if not response:
            return {"success": False, "data": None}

        return {"success": True, "data": create_album_payload(response)}
