from fastapi import HTTPException
from common.helpers import use_fetch
from common.constants import ENDPOINTS
from modules.search.helper import create_search_payload

class SearchAllUseCase:
    def execute(self, query: str):
        params = {"query": query}
        data = use_fetch(ENDPOINTS['search']['all'], params)
        if not data:
            raise HTTPException(status_code=404, detail=f"No results found for {query}")
        return create_search_payload(data)
