import re
from typing import List, Dict, Any
from modules.artists.mappers import create_artist_map_payload
from common.helpers import create_image_links

def get_int_or_none(value):
    if value is None or value == '':
        return None
    return int(value)

def create_search_payload(search: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'topQuery': {
            'results': [
                {
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'image': create_image_links(item.get('image')),
                    'album': item.get('more_info', {}).get('album'),
                    'url': item.get('perma_url'),
                    'type': item.get('type'),
                    'language': item.get('more_info', {}).get('language'),
                    'description': item.get('description'),
                    'primaryArtists': item.get('more_info', {}).get('primary_artists'),
                    'singers': item.get('more_info', {}).get('singers')
                }
                for item in search.get('topquery', {}).get('data', [])
            ],
            'position': search.get('topquery', {}).get('position')
        },
        'songs': {
            'results': [
                {
                    'id': song.get('id'),
                    'title': song.get('title'),
                    'image': create_image_links(song.get('image')),
                    'album': song.get('more_info', {}).get('album'),
                    'url': song.get('perma_url'),
                    'type': song.get('type'),
                    'description': song.get('description'),
                    'primaryArtists': song.get('more_info', {}).get('primary_artists'),
                    'singers': song.get('more_info', {}).get('singers'),
                    'language': song.get('more_info', {}).get('language')
                }
                for song in search.get('songs', {}).get('data', [])
            ],
            'position': search.get('songs', {}).get('position')
        },
        'albums': {
            'results': [
                {
                    'id': album.get('id'),
                    'title': album.get('title'),
                    'image': create_image_links(album.get('image')),
                    'artist': album.get('more_info', {}).get('music'),
                    'url': album.get('perma_url'),
                    'type': album.get('type'),
                    'description': album.get('description'),
                    'year': album.get('more_info', {}).get('year'),
                    'songIds': album.get('more_info', {}).get('song_pids'),
                    'language': album.get('more_info', {}).get('language')
                }
                for album in search.get('albums', {}).get('data', [])
            ],
            'position': search.get('albums', {}).get('position')
        },
        'artists': {
            'results': [
                {
                    'id': artist.get('id'),
                    'title': artist.get('title'),
                    'image': create_image_links(artist.get('image')),
                    'type': artist.get('type'),
                    'description': artist.get('description'),
                    'position': artist.get('position')
                }
                for artist in search.get('artists', {}).get('data', [])
            ],
            'position': search.get('artists', {}).get('position')
        },
        'playlists': {
            'results': [
                {
                    'id': playlist.get('id'),
                    'title': playlist.get('title'),
                    'image': create_image_links(playlist.get('image')),
                    'url': playlist.get('perma_url'),
                    'type': playlist.get('type'),
                    'language': playlist.get('more_info', {}).get('language'),
                    'description': playlist.get('description')
                }
                for playlist in search.get('playlists', {}).get('data', [])
            ],
            'position': search.get('playlists', {}).get('position')
        }
    }

def create_search_playlist_payload(playlist: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'id': playlist.get('id'),
        'name': playlist.get('title'),
        'type': playlist.get('type'),
        'image': create_image_links(playlist.get('image')),
        'url': playlist.get('perma_url'),
        'songCount': get_int_or_none(playlist.get('more_info', {}).get('song_count')),
        'language': playlist.get('more_info', {}).get('language'),
        'explicitContent': playlist.get('explicit_content') == '1'
    }

def create_search_album_payload(album: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'total': get_int_or_none(album.get('total')),
        'start': get_int_or_none(album.get('start')),
        'results': [
            {
                'id': item.get('id'),
                'name': item.get('title'),
                'description': item.get('header_desc'),
                'url': item.get('perma_url'),
                'year': get_int_or_none(item.get('year')),
                'type': item.get('type'),
                'playCount': get_int_or_none(item.get('play_count')),
                'language': item.get('language'),
                'explicitContent': item.get('explicit_content') == '1',
                'artists': {
                    'primary': [create_artist_map_payload(artist) for artist in item.get('more_info', {}).get('artistMap', {}).get('primary_artists', [])],
                    'featured': [create_artist_map_payload(artist) for artist in item.get('more_info', {}).get('artistMap', {}).get('featured_artists', [])],
                    'all': [create_artist_map_payload(artist) for artist in item.get('more_info', {}).get('artistMap', {}).get('artists', [])]
                },
                'image': create_image_links(item.get('image'))
            }
            for item in album.get('results', [])
        ]
    }
