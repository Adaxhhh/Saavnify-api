from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modules.songs.models import Song
    from modules.albums.models import Album

class ArtistBio(BaseModel):
    text: str
    title: str
    sequence: int

class Artist(BaseModel):
    id: str
    name: str
    url: str
    type: str
    follower_count: Optional[int] = Field(None, alias="followerCount")
    fan_count: Optional[str] = Field(None, alias="fanCount")
    is_verified: Optional[bool] = Field(None, alias="isVerified")
    dominant_language: Optional[str] = Field(None, alias="dominantLanguage")
    dominant_type: Optional[str] = Field(None, alias="dominantType")
    bio: Optional[List[ArtistBio]] = None
    dob: Optional[str] = None
    fb: Optional[str] = None
    twitter: Optional[str] = None
    wiki: Optional[str] = None
    available_languages: Optional[List[str]] = Field(None, alias="availableLanguages")
    is_radio_present: Optional[bool] = Field(None, alias="isRadioPresent")
    image: list
    top_songs: Optional[List[Any]] = Field(None, alias="topSongs")
    top_albums: Optional[List[Any]] = Field(None, alias="topAlbums")
    singles: Optional[List[Any]] = None
    similar_artists: Optional[List[Any]] = Field(None, alias="similarArtists")
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class ArtistSong(BaseModel):
    total: int
    songs: List[Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class ArtistAlbum(BaseModel):
    total: int
    albums: List[Any]
    
    model_config = ConfigDict(arbitrary_types_allowed=True)

class ArtistMap(BaseModel):
    id: str
    name: str
    role: str
    image: list
    type: str
    url: str
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
