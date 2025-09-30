from fastapi import APIRouter, HTTPException, Query, Depends, Path
from typing import Optional
import re
from pydantic import BaseModel, validator

from modules.songs.service import SongService
from common.models import ResponseModel, ErrorResponse

router = APIRouter(prefix="/api")
song_service = SongService()

class SongQuery(BaseModel):
    ids: Optional[str] = None
    link: Optional[str] = None

    @validator('link')
    def validate_link(cls, v):
        if v:
            match = re.search(r'jiosaavn.com/song/[^/]+/([^/]+)$', v)
            if not match:
                raise HTTPException(status_code=400, detail='Invalid song link')
            return match.group(1)
        return v

@router.get("/songs")
def get_songs(query: SongQuery = Depends()):
    if not query.ids and not query.link:
        raise HTTPException(status_code=400, detail="Either 'ids' or 'link' query parameter must be provided")

    try:
        if query.link:
            return ResponseModel(success=True, data=song_service.get_song_by_link(query.link))

        if query.ids:
            return ResponseModel(success=True, data=song_service.get_song_by_ids(query.ids))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/songs/{song_id}")
def get_song_by_id(song_id: str = Path(..., title="Song ID", description="ID of the song to retrieve")):
    try:
        return ResponseModel(success=True, data=song_service.get_song_by_ids(song_id))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

class SuggestionsQuery(BaseModel):
    limit: int = Query(10, title="Limit", description="Limit the number of suggestions to retrieve")

@router.get("/songs/{song_id}/suggestions")
def get_song_suggestions(song_id: str = Path(..., title="Song ID", description="ID of the song to retrieve suggestions for"),
                         query: SuggestionsQuery = Depends()):
    try:
        return ResponseModel(success=True, data=song_service.get_song_suggestions(song_id, query.limit))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
