'''
Docstring
'''

import json


class Artist:
    '''
    Object that represents an `Artist` -- a creator of one or more `songs`.
    '''

    def __init__(self, id, resp_json):
        '''
        Creates Artist object
        '''
        self._id = id
        self._artist_dict = resp_json['artist']

    @property
    def id(self):
        '''ID of artist -> int'''
        return self._id

    @property
    def alternate_names(self):
        '''Aliases for artist's name -> list'''
        return self._artist_dict['alternate_names']

    @property
    def api_path(self):
        '''
        Web path of artist -> str

        e.g. '/artist/16775'
        '''
        return self._artist_dict['api_path']

    @property
    def description(self):
        '''
        Song description -> dict

        Structure of dictionary depends on the text_format paramater sent.
        '''
        return self._artist_dict['description']

    @property
    def facebook_name(self):
        '''Facebook username -> str'''
        return self._artist_dict['facebook_name']

    @property
    def followers_count(self):
        '''Number of followers on Genius -> int'''
        return self._artist_dict['followers_count']

    @property
    def header_image_url(self):
        '''URL of header image used on profile -> str'''
        return self._artist_dict['header_image_url']

    @property
    def image_url(self):
        '''URL of profile image -> str'''
        return self._artist_dict['image_url']

    @property
    def instagram_name(self):
        '''Instagram username -> str'''
        return self._artist_dict['instagram_name']

    @property
    def is_meme_verified(self):
        '''I don't know what meme verified means... -> bool'''
        return self._artist_dict['is_meme_verified']

    @property
    def is_verified(self):
        '''Check whether artist has verified their profile -> bool'''
        return self._artist_dict['is_verified']

    @property
    def name(self):
        '''Artist name -> str'''
        return self._artist_dict['name']

    @property
    def url(self):
        '''URL of profile on Genius -> str'''
        return self._artist_dict['url']

    @property
    def current_user_metadata(self):
        '''Metadata on relationship between you and artist -> dict'''
        return self._artist_dict['current_user_metadata']

    @property
    def description_annotation(self):
        '''Info on the artist description (which is an annotation) -> dict'''
        return self._artist_dict['description_annotation']

    @property
    def user(self):
        '''? -> ?'''
        return self._artist_dict['user']

    def __repr__(self):
        return 'Artist({}:{})'.format(self._id, self.name)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self._artist_dict
