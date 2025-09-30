import json
from urllib.parse import quote

from common.helpers import use_fetch

class CreateSongStationUseCase:
    def execute(self, song_id: str):
        encoded_song_id = json.dumps([quote(song_id)])
        
        response = use_fetch(
            'webradio.createEntityStation',
            {
                'entity_id': encoded_song_id,
                'entity_type': 'queue'
            },
            context='android'
        )
        
        if 'stationid' not in response:
            return None
            
        return response['stationid']
