from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Any

class DownloadLink(BaseModel):
    quality: str
    url: str
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class ArtistMap(BaseModel):
    id: str
    name: str
    role: str
    type: str
    image: List[Any]
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

class SearchSong(BaseModel):
    total: int
    start: int
    results: List[Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class SearchAlbum(BaseModel):
    id: str
    name: str
    description: str
    year: Optional[int] = None
    type: str
    play_count: Optional[int] = Field(None, alias="playCount")
    language: str
    explicit_content: bool = Field(..., alias="explicitContent")
    artists: dict
    url: str
    image: List[Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class SearchArtist(BaseModel):
    id: str
    name: str
    role: str
    type: str
    image: List[Any]
    url: str
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class SearchPlaylist(BaseModel):
    id: str
    name: str
    type: str
    image: List[Any]
    url: str
    song_count: Optional[int] = Field(None, alias="songCount")
    language: str
    explicit_content: bool = Field(..., alias="explicitContent")
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class SearchAll(BaseModel):
    albums: List[Any]
    songs: List[Any]
    artists: List[Any]
    playlists: List[Any]
    top_query: List[dict] = Field(..., alias="topQuery")
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
