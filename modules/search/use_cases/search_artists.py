from fastapi import HTTPException
from common.constants import ENDPOINTS
from common.helpers import use_fetch
from modules.artists.mappers import create_artist_map_payload

class SearchArtistsUseCase:
    def execute(self, query: str, page: int, limit: int):
        response = use_fetch(ENDPOINTS['search']['artists'], {'q': query, 'p': page, 'n': limit})

        if not response:
            raise HTTPException(status_code=404, detail='artist not found')
        
        return {
            'total': response.get('total'),
            'start': response.get('start'),
            'results': [create_artist_map_payload(artist) for artist in response.get('results', [])]
        }
