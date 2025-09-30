from common.helpers import use_fetch
from modules.artists.helpers import create_artist_payload

class GetArtistByLinkUseCase:
    def execute(self, token: str, page: int, song_count: int, album_count: int, sort_by: str, sort_order: str):
        response = use_fetch(
            'webapi.get',
            {
                'token': token,
                'n_song': song_count,
                'n_album': album_count,
                'page': page,
                'sort_order': sort_order,
                'category': sort_by,
                'type': 'artist'
            }
        )
        
        if not response:
            return {"success": False, "data": None}

        return {"success": True, "data": create_artist_payload(response)}
