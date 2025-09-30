from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.songs.models import Song
    from modules.artists.models import ArtistMap

class AlbumArtist(BaseModel):
    primary: List[Any]
    featured: List[Any]
    all: List[Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class Album(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    type: str
    year: Optional[int] = None
    play_count: Optional[int] = Field(None, alias="playCount")
    language: str
    explicit_content: bool = Field(..., alias="explicitContent")
    url: str
    song_count: Optional[int] = Field(None, alias="songCount")
    artists: AlbumArtist
    image: list
    songs: Optional[List[Any]] = None
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
