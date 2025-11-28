import requests
import re
from typing import Dict, Any, List
import base64
from Crypto.Cipher import DES
import random

# User agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) obsidian/1.8.4 Chrome/130.0.6723.191 Electron/33.3.2 Safari/537.36'
]

def use_fetch(endpoint: str, params: Dict[str, Any], context: str = 'web6dot0') -> Dict[str, Any]:
    url = "https://www.jiosaavn.com/api.php"

    default_params = {
        "__call": endpoint,
        "_format": "json",
        "_marker": "0",
        "api_version": "4",
        "ctx": context
        "_locale": "en_US"
        "country": "US"
    }

    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, params={**default_params, **params}, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from JioSaavn API: {str(e)}")

def create_download_links(encrypted_media_url: str) -> List[Dict[str, str]]:
    if not encrypted_media_url:
        return []

    qualities = [
        { 'id': '_12', 'bitrate': '12kbps' },
        { 'id': '_48', 'bitrate': '48kbps' },
        { 'id': '_96', 'bitrate': '96kbps' },
        { 'id': '_160', 'bitrate': '160kbps' },
        { 'id': '_320', 'bitrate': '320kbps' }
    ]

    key = '38346591'.encode()

    try:
        encrypted = base64.b64decode(encrypted_media_url.strip())
    except Exception:
        return []

    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(encrypted)
    # Remove PKCS5/PKCS7 padding - strip all control characters from the end
    decrypted_link = decrypted_bytes.decode('utf-8')
    # Strip all ASCII control characters (0x00-0x1F) from the end
    while decrypted_link and ord(decrypted_link[-1]) < 32:
        decrypted_link = decrypted_link[:-1]

    return [
        {
            'quality': quality['bitrate'],
            'url': decrypted_link.replace('_96', quality['id'])
        }
        for quality in qualities
    ]

def create_image_links(link: str) -> List[Dict[str, str]]:
    if not link:
        return []

    qualities = ['50x50', '150x150', '500x500']
    quality_regex = r"150x150|50x50"
    protocol_regex = r"^http://"

    return [
        {
            'quality': quality,
            'url': re.sub(protocol_regex, 'https://', re.sub(quality_regex, quality, link))
        }
        for quality in qualities
    ]