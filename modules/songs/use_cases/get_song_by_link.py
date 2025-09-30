from common.helpers import use_fetch
from modules.songs.mappers import create_song_payload

class GetSongByLinkUseCase:
    def execute(self, token: str):
        response = use_fetch('webapi.get', {'token': token, 'type': 'song'})

        if 'songs' not in response or not response['songs']:
            raise Exception("Song not found")

        songs = [create_song_payload(song) for song in response['songs']]
        return songs
