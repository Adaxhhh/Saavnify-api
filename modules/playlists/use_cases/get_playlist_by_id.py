from common.helpers import use_fetch
from modules.playlists.helpers import create_playlist_payload

class GetPlaylistByIdUseCase:
    def execute(self, playlist_id: str, limit: int, page: int):
        response = use_fetch(
            'playlist.getDetails',
            {
                'listid': playlist_id,
                'n': limit,
                'p': page
            }
        )
        
        if not response:
            return {"success": False, "data": None}

        playlist = create_playlist_payload(response)
        
        if playlist and playlist.get('songs'):
            playlist['songs'] = playlist['songs'][:limit]
        
        return {"success": True, "data": playlist}
