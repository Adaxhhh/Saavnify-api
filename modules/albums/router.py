from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
import re
from pydantic import BaseModel, validator

from modules.albums.service import AlbumService
from modules.albums.models import Album
from common.models import ResponseModel

router = APIRouter(prefix="/api")
album_service = AlbumService()

class AlbumQuery(BaseModel):
    id: Optional[str] = None
    link: Optional[str] = None

    @validator('link')
    def validate_link(cls, v):
        if v:
            match = re.search(r'jiosaavn.com/album/[^/]+/([^/]+)', v)
            if not match:
                raise HTTPException(status_code=400, detail='Invalid album link')
            return match.group(1)
        return v

@router.get("/albums")
def get_albums(query: AlbumQuery = Depends()):
    if not query.id and not query.link:
        raise HTTPException(status_code=400, detail="Either 'id' or 'link' query parameter must be provided")

    try:
        if query.link:
            return ResponseModel(success=True, data=album_service.get_album_by_link(query.link))

        if query.id:
            return ResponseModel(success=True, data=album_service.get_album_by_id(query.id))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
