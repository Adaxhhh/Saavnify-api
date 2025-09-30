from common.helpers import use_fetch
from common.constants import ENDPOINTS
from modules.songs.mappers import create_song_payload

class SearchSongsUseCase:
    def execute(self, query: str, page: int, limit: int):
        params = {"q": query, "p": page, "n": limit}
        data = use_fetch(ENDPOINTS['search']['songs'], params)

        return {
            "total": data.get('total'),
            "start": data.get('start'),
            "results": [create_song_payload(song) for song in data.get('results', [])]
        }
