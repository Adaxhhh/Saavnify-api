from common.helpers import use_fetch
from modules.playlists.helpers import create_playlist_payload

class GetPlaylistByLinkUseCase:
    def execute(self, token: str, limit: int, page: int):
        response = use_fetch(
            'webapi.get',
            {
                'token': token,
                'n': limit,
                'p': page,
                'type': 'playlist'
            }
        )
        
        if not response:
            return {"success": False, "data": None}

        playlist = create_playlist_payload(response)
        
        if playlist and playlist.get('songs'):
            playlist['songs'] = playlist['songs'][:limit]
        
        return {"success": True, "data": playlist}
