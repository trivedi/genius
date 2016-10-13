import json


class Account:
    '''
    Object that represents a `song` -- an annotatable document hosted on Genius

    Data for a song includes details about the document and information about
    the referents that are attached to it.
    '''
    def __init__(self, resp_json):
        '''
        Creates Account object

        Account information includes general contact information and
        Genius-specific details about a user
        '''
        self._account_dict = resp_json['user']

    @property
    def id(self):
        '''ID of user -> int'''
        return self._account_dict['id']

    @property
    def about_me(self):
        '''
        Personal description of user -> dict

        Structure of dictionary depends on the text_format parameter sent
        '''
        return self._account_dict['about_me']

    @property
    def api_path(self):
        '''
        Web path of user's profile -> str

        e.g. '/users/3737118'
        '''
        return self._api_path

    @property
    def available_identity_providers(self):
        '''Names of identity providers -> list'''
        return self._account_dict['available_identity_providers']

    @property
    def avatar(self):
        '''
        Image avatar information -> dict

        Keys:
        tiny -> url -> str
             -> bounding_box -> width  -> int
                             -> height -> int
        thumb ...
        small ...
        medium ...
        '''
        return self._account_dict['avatar']

    def __repr__(self):
        '''
        TODO: should probably separate full API response and the object's response
        '''
        pass
