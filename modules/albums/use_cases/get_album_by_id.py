from common.helpers import use_fetch
from modules.albums.helpers import create_album_payload

class GetAlbumByIdUseCase:
    def execute(self, album_id: str):
        response = use_fetch('content.getAlbumDetails', {'albumid': album_id})
        
        if not response:
            return {"success": False, "data": None}

        return {"success": True, "data": create_album_payload(response)}
