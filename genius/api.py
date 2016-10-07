'''
Docstring
'''

from rauth import OAuth2Session
from cred import *
from artist import *
from song import *

SESSION = OAuth2Session(CLIENT_ID, CLIENT_SECRET, CLIENT_ACCESS_TOKEN)
BASE_URI = 'https://api.genius.com'


def get_song(id, text_format='plain'):
    resource = '/songs/' + id
    params = {'text_format': text_format}
    resp = get_request(resource, params)
    return Song(id, resp.json().get('response'))


def get_request(resource, payload=None):
    url = '{}{}'.format(BASE_URI, resource)
    r = SESSION.get(url, params=payload)
    return r


print get_song('378195')
