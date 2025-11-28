import requests
import re
import base64
import random
from Crypto.Cipher import DES

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
]


def use_fetch(endpoint: str, params: dict, context: str = 'web6dot0'):
    url = "https://www.jiosaavn.com/api.php"

    default_params = {
        "__call": endpoint,
        "_format": "json",
        "_marker": "0",
        "api_version": "4",
        "ctx": context,
        "_locale": "en_US",
        "country": "US"
    }

    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }

    try:
        res = requests.get(url, params={**default_params, **params}, headers=headers, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        raise Exception(f"JioSaavn API error: {str(e)}")


def create_download_links(enc: str):
    if not enc:
        return []

    qualities = [
        {'id': '_12', 'bitrate': '12kbps'},
        {'id': '_48', 'bitrate': '48kbps'},
        {'id': '_96', 'bitrate': '96kbps'},
        {'id': '_160', 'bitrate': '160kbps'},
        {'id': '_320', 'bitrate': '320kbps'},
    ]

    key = b'38346591'

    try:
        encrypted = base64.b64decode(enc)
    except:
        return []

    cipher = DES.new(key, DES.MODE_ECB)
    dec = cipher.decrypt(encrypted)

    pad_len = dec[-1]
    dec = dec[:-pad_len]

    url = dec.decode()

    return [
        {
            'quality': q['bitrate'],
            'url': re.sub(r'_\d+', q['id'], url)
        }
        for q in qualities
    ]


def create_image_links(link: str):
    if not link:
        return []

    qualities = ['50x50', '150x150', '500x500']
    quality_regex = r"50x50|150x150|500x500"

    return [
        {
            'quality': q,
            'url': re.sub(r"^http://", "https://", re.sub(quality_regex, q, link))
        }
        for q in qualities
    ]
