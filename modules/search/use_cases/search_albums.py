from common.constants import ENDPOINTS
from common.helpers import use_fetch
from modules.search.helper import create_search_album_payload

class SearchAlbumsUseCase:
    def execute(self, query: str, page: int, limit: int):
        response = use_fetch(ENDPOINTS['search']['albums'], {'q': query, 'p': page, 'n': limit})
        
        return create_search_album_payload(response)
