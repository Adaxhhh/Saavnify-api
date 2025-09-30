from common.helpers import use_fetch
from modules.albums.helpers import create_album_payload

class GetArtistAlbumsUseCase:
    def execute(self, artist_id: str, page: int, sort_by: str, sort_order: str):
        response = use_fetch(
            'artist.getArtistMoreAlbum',
            {
                'artistId': artist_id,
                'page': page,
                'sort_order': sort_order,
                'category': sort_by
            }
        )
        
        if not response:
            return {"success": False, "data": None}

        return {
            "success": True,
            "data": {
                'total': response.get('topAlbums', {}).get('total'),
                'albums': [create_album_payload(album) for album in response.get('topAlbums', {}).get('albums', [])]
            }
        }
