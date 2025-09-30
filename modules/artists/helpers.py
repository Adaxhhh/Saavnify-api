import json
from common.helpers import create_image_links
from modules.albums.helpers import create_album_payload
from modules.songs.mappers import create_song_payload

def get_int_or_none(value):
    if value is None or value == '':
        return None
    return int(value)

def create_artist_payload(artist):
    return {
        'id': artist.get('artistId') or artist.get('id'),
        'name': artist.get('name'),
        'url': artist.get('urls', {}).get('overview') or artist.get('perma_url'),
        'type': artist.get('type'),
        'followerCount': get_int_or_none(artist.get('follower_count')),
        'fanCount': artist.get('fan_count'),
        'isVerified': artist.get('isVerified'),
        'dominantLanguage': artist.get('dominantLanguage'),
        'dominantType': artist.get('dominantType'),
        'bio': json.loads(artist['bio']) if artist.get('bio') else None,
        'dob': artist.get('dob'),
        'fb': artist.get('fb'),
        'twitter': artist.get('twitter'),
        'wiki': artist.get('wiki'),
        'availableLanguages': artist.get('availableLanguages'),
        'isRadioPresent': artist.get('isRadioPresent'),
        'image': create_image_links(artist.get('image')),
        'topSongs': [create_song_payload(song) for song in artist.get('topSongs', [])] if artist.get('topSongs') else None,
        'topAlbums': [create_album_payload(album) for album in artist.get('topAlbums', [])] if artist.get('topAlbums') else None,
        'singles': [create_song_payload(song) for song in artist.get('singles', [])] if artist.get('singles') else None,
        'similarArtists': [
            {
                'id': similar_artist.get('id'),
                'name': similar_artist.get('name'),
                'url': similar_artist.get('perma_url'),
                'image': create_image_links(similar_artist.get('image_url')),
                'languages': json.loads(similar_artist['languages']) if similar_artist.get('languages') else None,
                'wiki': similar_artist.get('wiki'),
                'dob': similar_artist.get('dob'),
                'fb': similar_artist.get('fb'),
                'twitter': similar_artist.get('twitter'),
                'isRadioPresent': similar_artist.get('isRadioPresent'),
                'type': similar_artist.get('type'),
                'dominantType': similar_artist.get('dominantType'),
                'aka': similar_artist.get('aka'),
                'bio': json.loads(similar_artist['bio']) if similar_artist.get('bio') else None,
                'similarArtists': json.loads(similar_artist['similar']) if similar_artist.get('similar') else None,
            }
            for similar_artist in artist.get('similarArtists', [])
        ] if artist.get('similarArtists') else None
    }
