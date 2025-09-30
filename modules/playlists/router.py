from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional
import re
from pydantic import BaseModel, validator

from modules.playlists.service import PlaylistService
from modules.playlists.models import Playlist
from common.models import ResponseModel

router = APIRouter(prefix="/api")
playlist_service = PlaylistService()

class PlaylistQuery(BaseModel):
    id: Optional[str] = None
    link: Optional[str] = None
    page: int = 0
    limit: int = 10

    @validator('link')
    def validate_link(cls, v):
        if v:
            matches = re.search(r'(?:jiosaavn.com|saavn.com)/(?:featured|s/playlist)/[^/]+/([^/]+)$|/([^/]+)$', v)
            if not matches:
                raise HTTPException(status_code=400, detail='Invalid playlist link')
            
            filtered_matches = [match for match in matches.groups() if match is not None]
            return filtered_matches[-1] if filtered_matches else None
        return v

@router.get("/playlists")
def get_playlists(query: PlaylistQuery = Depends()):
    if not query.id and not query.link:
        raise HTTPException(status_code=400, detail="Either 'id' or 'link' query parameter must be provided")

    try:
        if query.link:
            return ResponseModel(success=True, data=playlist_service.get_playlist_by_link(query.link, query.limit, query.page))

        if query.id:
            return ResponseModel(success=True, data=playlist_service.get_playlist_by_id(query.id, query.limit, query.page))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
