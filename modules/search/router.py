from fastapi import APIRouter, HTTPException
from modules.search.service import SearchService
from modules.search.models import SearchSong, SearchAlbum, SearchArtist, SearchPlaylist, SearchAll
from common.models import ResponseModel

router = APIRouter(prefix="/api")
search_service = SearchService()

@router.get("/search/songs")
def search_songs(query: str, page: int = 0, limit: int = 10):
    try:
        return ResponseModel(success=True, data=search_service.search_songs(query, page, limit))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/albums")
def search_albums(query: str, page: int = 0, limit: int = 10):
    try:
        return ResponseModel(success=True, data=search_service.search_albums(query, page, limit))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/artists")
def search_artists(query: str, page: int = 0, limit: int = 10):
    try:
        return ResponseModel(success=True, data=search_service.search_artists(query, page, limit))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/playlists")
def search_playlists(query: str, page: int = 0, limit: int = 10):
    try:
        return ResponseModel(success=True, data=search_service.search_playlists(query, page, limit))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
def search_all(query: str):
    try:
        return ResponseModel(success=True, data=search_service.search_all(query))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
