from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Any

class DownloadLink(BaseModel):
    quality: str
    url: str
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class Song(BaseModel):
    id: str
    name: str
    type: str
    year: Optional[str] = None
    release_date: Optional[str] = Field(None, alias="releaseDate")
    duration: Optional[int] = None
    label: Optional[str] = None
    explicit_content: bool = Field(..., alias="explicitContent")
    play_count: Optional[int] = Field(None, alias="playCount")
    language: str
    has_lyrics: bool = Field(..., alias="hasLyrics")
    lyrics_id: Optional[str] = Field(None, alias="lyricsId")
    url: str
    copyright: Optional[str] = None
    album: dict
    artists: dict
    image: List[Any]
    download_url: List[Any] = Field(..., alias="downloadUrl")
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
