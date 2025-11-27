from fastapi import FastAPI
from modules.albums.router import router as albums_router
from modules.artists.router import router as artists_router
from modules.playlists.router import router as playlists_router
from modules.search.router import router as search_router
from modules.songs.router import router as songs_router

app = FastAPI(
    title="JioSaavn API",
    description="Unofficial JioSaavn API - Python implementation",
    version="0.1.0"
)

app.include_router(albums_router)
app.include_router(artists_router)
app.include_router(playlists_router)
app.include_router(search_router)
app.include_router(songs_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
