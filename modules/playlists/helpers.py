from common.helpers import create_image_links
from modules.artists.mappers import create_artist_map_payload
from modules.songs.mappers import create_song_payload

def get_int_or_none(value):
    if value is None or value == '':
        return None
    return int(value)

def create_playlist_payload(playlist):
    return {
        'id': playlist.get('id'),
        'name': playlist.get('title'),
        'description': playlist.get('header_desc'),
        'type': playlist.get('type'),
        'year': get_int_or_none(playlist.get('year')),
        'playCount': get_int_or_none(playlist.get('play_count')),
        'language': playlist.get('language'),
        'explicitContent': playlist.get('explicit_content') == '1',
        'url': playlist.get('perma_url'),
        'songCount': get_int_or_none(playlist.get('list_count')),
        'artists': [create_artist_map_payload(artist) for artist in playlist.get('more_info', {}).get('artists', [])] if playlist.get('more_info', {}).get('artists') else None,
        'image': create_image_links(playlist.get('image')),
        'songs': [create_song_payload(song) for song in playlist.get('list', [])] if playlist.get('list') else None
    }
