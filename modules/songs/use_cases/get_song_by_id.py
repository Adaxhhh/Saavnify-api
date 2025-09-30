from common.helpers import use_fetch
from modules.songs.mappers import create_song_payload

class GetSongByIdUseCase:
    def execute(self, song_ids: str):
        response = use_fetch('song.getDetails', {'pids': song_ids})

        if 'songs' not in response or not response['songs']:
            raise Exception("Song not found")

        songs = [create_song_payload(song) for song in response['songs']]
        return songs
