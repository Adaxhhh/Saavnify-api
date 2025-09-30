from common.helpers import use_fetch
from modules.songs.mappers import create_song_payload
from modules.songs.use_cases.create_song_station import CreateSongStationUseCase

class GetSongSuggestionsUseCase:
    def __init__(self):
        self.create_song_station_use_case = CreateSongStationUseCase()

    def execute(self, song_id: str, limit: int):
        station_id = self.create_song_station_use_case.execute(song_id)

        if not station_id:
            return []

        response = use_fetch(
            'webradio.getSong',
            {
                'stationid': station_id,
                'k': limit
            },
            context='android'
        )

        if not response:
            return []

        suggestions = [
            create_song_payload(value['song'])
            for key, value in response.items()
            if key.isdigit() and 'song' in value
        ]

        return suggestions[:limit]
