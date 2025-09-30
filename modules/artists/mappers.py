from common.helpers import create_image_links

def create_artist_map_payload(artist):
    return {
        'id': artist.get('id'),
        'name': artist.get('name'),
        'role': artist.get('role'),
        'image': create_image_links(artist.get('image')),
        'type': artist.get('type'),
        'url': artist.get('perma_url')
    }
