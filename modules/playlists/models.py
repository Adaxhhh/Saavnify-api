from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Any

class Playlist(BaseModel):
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
    artists: Optional[List[Any]] = None
    image: list
    songs: Optional[List[Any]] = None
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
