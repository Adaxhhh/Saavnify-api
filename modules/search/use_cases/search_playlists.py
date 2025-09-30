from fastapi import HTTPException
from common.constants import ENDPOINTS
from common.helpers import use_fetch
from modules.search.helper import create_search_playlist_payload

class SearchPlaylistsUseCase:
    def execute(self, query: str, page: int, limit: int):
        response = use_fetch(ENDPOINTS['search']['playlists'], {'q': query, 'p': page, 'n': limit})

        if not response:
            raise HTTPException(status_code=404, detail='playlist not found')
        
        return create_search_playlist_payload(response)
