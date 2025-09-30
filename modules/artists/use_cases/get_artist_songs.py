from common.helpers import use_fetch
from modules.songs.mappers import create_song_payload

class GetArtistSongsUseCase:
    def execute(self, artist_id: str, page: int, sort_by: str, sort_order: str):
        response = use_fetch(
            'artist.getArtistMoreSong',
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
                'total': response.get('topSongs', {}).get('total'),
                'songs': [create_song_payload(song) for song in response.get('topSongs', {}).get('songs', [])]
            }
        }
