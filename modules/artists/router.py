from fastapi import APIRouter, HTTPException, Depends, Path, Query
from typing import Optional
import re
from pydantic import BaseModel, validator
from enum import Enum

from modules.artists.service import ArtistService
from modules.artists.models import Artist, ArtistSong, ArtistAlbum
from common.models import ResponseModel

router = APIRouter(prefix="/api")
artist_service = ArtistService()

class SortBy(str, Enum):
    popularity = "popularity"
    latest = "latest"
    alphabetical = "alphabetical"

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class ArtistQuery(BaseModel):
    id: Optional[str] = None
    link: Optional[str] = None
    page: int = 0
    song_count: int = 10
    album_count: int = 10
    sort_by: SortBy = 'popularity'
    sort_order: SortOrder = 'desc'

    @validator('link')
    def validate_link(cls, v):
        if v:
            match = re.search(r'jiosaavn.com/artist/[^/]+/([^/]+)$', v)
            if not match:
                raise HTTPException(status_code=400, detail='Invalid artist link')
            return match.group(1)
        return v

@router.get("/artists")
def get_artists(query: ArtistQuery = Depends()):
    if not query.id and not query.link:
        raise HTTPException(status_code=400, detail="Either 'id' or 'link' query parameter must be provided")

    try:
        if query.link:
            return ResponseModel(success=True, data=artist_service.get_artist_by_link(
                query.link, query.page, query.song_count, query.album_count, query.sort_by, query.sort_order
            ))

        if query.id:
            return ResponseModel(success=True, data=artist_service.get_artist_by_id(
                query.id, query.page, query.song_count, query.album_count, query.sort_by, query.sort_order
            ))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/artists/{artist_id}")
def get_artist_by_id(
    artist_id: str = Path(..., title="Artist ID", description="ID of the artist to retrieve"),
    page: int = Query(0, title="Page number"),
    song_count: int = Query(10, title="Song count"),
    album_count: int = Query(10, title="Album count"),
    sort_by: SortBy = Query('popularity', title="Sort by"),
    sort_order: SortOrder = Query('desc', title="Sort order")
):
    try:
        return ResponseModel(success=True, data=artist_service.get_artist_by_id(
            artist_id, page, song_count, album_count, sort_by, sort_order
        ))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/artists/{artist_id}/songs")
def get_artist_songs(
    artist_id: str = Path(..., title="Artist ID", description="ID of the artist to retrieve songs for"),
    page: int = Query(0, title="Page number"),
    sort_by: SortBy = Query('popularity', title="Sort by"),
    sort_order: SortOrder = Query('desc', title="Sort order")
):
    try:
        return ResponseModel(success=True, data=artist_service.get_artist_songs(
            artist_id, page, sort_by, sort_order
        ))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/artists/{artist_id}/albums")
def get_artist_albums(
    artist_id: str = Path(..., title="Artist ID", description="ID of the artist to retrieve albums for"),
    page: int = Query(0, title="Page number"),
    sort_by: SortBy = Query('popularity', title="Sort by"),
    sort_order: SortOrder = Query('desc', title="Sort order")
):
    try:
        return ResponseModel(success=True, data=artist_service.get_artist_albums(
            artist_id, page, sort_by, sort_order
        ))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
