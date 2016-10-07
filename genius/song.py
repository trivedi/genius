import json

class Song:
    '''
    Object that represents a `song` -- an annotatable document hosted on Genius

    Data for a song includes details about the document and information about
    the referents that are attached to it.
    '''
    def __init__(self, id, resp_json):
        '''
        Creates Song object

        id = song id
        '''
        self.id = id
        self.resp_json = resp_json
        self.title = resp_json['song']['title']
        self.lyrics_owner = resp_json['song']['lyrics_owner_id']
        self.rel_path = resp_json['song']['path']

    def get_id(self):
        return self.id

    def get_url(self):
        return 'https://genius.com' + self.rel_path

    def __repr__(self):
        '''
        TODO: should probably separate full API response and the object's response
        '''
        return json.dumps(self.resp_json)
