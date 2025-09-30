from common.helpers import use_fetch
from modules.artists.helpers import create_artist_payload

class GetArtistByIdUseCase:
    def execute(self, artist_id: str, page: int, song_count: int, album_count: int, sort_by: str, sort_order: str):
        response = use_fetch(
            'artist.getArtistPageDetails',
            {
                'artistId': artist_id,
                'n_song': song_count,
                'n_album': album_count,
                'page': page,
                'sort_order': sort_order,
                'category': sort_by
            }
        )
        
        if not response:
            return {"success": False, "data": None}

        return {"success": True, "data": create_artist_payload(response)}
