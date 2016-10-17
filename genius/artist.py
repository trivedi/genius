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
        self.id = id
        self.resp_json = resp_json

    def get_id(self):
        return self.id

    def get_songs(self, id, sort='title', per_page=20, page=1):
        pass

    def __repr__(self):
        return json.dumps(self.resp_json)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return 'unicode representation'
