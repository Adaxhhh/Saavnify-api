from common.helpers import create_image_links, create_download_links
from modules.artists.mappers import create_artist_map_payload

def create_song_payload(song):
    more_info = song.get('more_info', {})
    artist_map = more_info.get('artistMap', {})
    
    # Convert duration and playCount to numbers, matching TypeScript behavior
    duration = more_info.get('duration')
    duration = int(duration) if duration else None
    
    play_count = song.get('play_count')
    play_count = int(play_count) if play_count else None
    
    # Process artists through the mapper, matching TypeScript implementation
    primary_artists = artist_map.get('primary_artists', [])
    featured_artists = artist_map.get('featured_artists', [])
    all_artists = artist_map.get('artists', [])
    
    return {
        'id': song.get('id'),
        'name': song.get('title'),
        'type': song.get('type'),
        'year': song.get('year') or None,
        'releaseDate': more_info.get('release_date') or None,
        'duration': duration,
        'label': more_info.get('label') or None,
        'explicitContent': song.get('explicit_content') == '1',
        'playCount': play_count,
        'language': song.get('language'),
        'hasLyrics': more_info.get('has_lyrics') == 'true',
        'lyricsId': more_info.get('lyrics_id') or None,
        'url': song.get('perma_url'),
        'copyright': more_info.get('copyright_text') or None,
        'album': {
            'id': more_info.get('album_id') or None,
            'name': more_info.get('album') or None,
            'url': more_info.get('album_url') or None
        },
        'artists': {
            'primary': [create_artist_map_payload(artist) for artist in primary_artists] if primary_artists else [],
            'featured': [create_artist_map_payload(artist) for artist in featured_artists] if featured_artists else [],
            'all': [create_artist_map_payload(artist) for artist in all_artists] if all_artists else []
        },
        'image': create_image_links(song.get('image')),
        'downloadUrl': create_download_links(more_info.get('encrypted_media_url'))
    }
