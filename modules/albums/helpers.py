from common.helpers import create_image_links
from modules.artists.mappers import create_artist_map_payload
from modules.songs.mappers import create_song_payload

def get_int_or_none(value):
    if value is None or value == '':
        return None
    return int(value)

def create_album_payload(album: dict) -> dict:
    return {
        'id': album.get('id'),
        'name': album.get('title'),
        'description': album.get('header_desc'),
        'type': album.get('type'),
        'year': get_int_or_none(album.get('year')),
        'playCount': get_int_or_none(album.get('play_count')),
        'language': album.get('language'),
        'explicitContent': album.get('explicit_content') == '1',
        'url': album.get('perma_url'),
        'songCount': get_int_or_none(album.get('more_info', {}).get('song_count')),
        'artists': {
            'primary': [create_artist_map_payload(artist) for artist in album.get('more_info', {}).get('artistMap', {}).get('primary_artists', [])],
            'featured': [create_artist_map_payload(artist) for artist in album.get('more_info', {}).get('artistMap', {}).get('featured_artists', [])],
            'all': [create_artist_map_payload(artist) for artist in album.get('more_info', {}).get('artistMap', {}).get('artists', [])]
        },
        'image': create_image_links(album.get('image')),
        'songs': [create_song_payload(song) for song in album.get('list', [])] if album.get('list') else None
    }
