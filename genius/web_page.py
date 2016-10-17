import json


class WebPage:
    '''
    Object that represents a `song` -- an annotatable document hosted on Genius

    Data for a song includes details about the document and information about
    the referents that are attached to it.
    '''
    def __init__(self, resp_json):
        '''
        Creates Web Page object

        A web page is a single, publicly accessible page to which annotations
        may be attached. Web pages map 1-to-1 with unique, canonical URLs.
        '''
        self._page_dict = resp_json['web_page']

    @property
    def annotation_count(self):
        '''Number of annotations on page -> int'''
        return self._page_dict['annotation_count']

    @property
    def domain(self):
        '''
        Domain of web page -> str

        e.g. 'genius.com'
        '''
        return self._page_dict['domain']

    @property
    def id(self):
        return self._page_dict['id']

    @property
    def normalized_url(self):
        '''
        Normalized URL of web page -> str

        e.g. '//genius.com/Kendrick-lamar-alright-lyrics'
        '''
        return self._page_dict['normalized_url']

    @property
    def share_url(self):
        '''URL of public annotatable web page (i.e. genius.it/url)'''
        return self._page_dict['share_url']

    @property
    def title(self):
        '''
        Title of page defined by  <title></title> -> str
        '''
        return self._page_dict['title']

    @property
    def url(self):
        '''URL of web page -> str'''
        return self._page_dict['url']

    def __repr__(self):
        '''
        TODO: should probably separate full API response and the object's response
        '''
        pass

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return 'unicode representation'
