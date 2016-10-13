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
        self._id = id
        self._song_dict = resp_json['song']
        self.title = resp_json['song']['title']
        self.lyrics_owner = resp_json['song']['lyrics_owner_id']
        self.rel_path = resp_json['song']['path']

    @property
    def id(self):
        '''ID of song -> str'''
        return self._id

    @property
    def annotation_count(self):
        return self._song_dict['annotation_count']

    @property
    def description(self):
        '''
        Song description -> dict

        Structure of dictionary depends on the text_format paramater sent.
        Same as the body of the description_annotation.

        '''
        return self._song_dict['description']

    @property
    def embed_content(self):
        '''Embedded content of song -> str'''
        return self._song_dict['embed_content']

    @property
    def fact_track(self):
        '''
        Fact Track is the Genius integration in the Spotify mobile app.
        Gives access to facts about this song that is being streamed -> str
        '''
        return self._song_dict['fact_track']

    @property
    def featured_video(self):
        '''Return whether song has a video on its page -> bool'''
        return self._song_dict['featured_video']

    @property
    def header_image_thumbnail_url(self):
        '''URL for the song's header thumbnail image (300x300) -> str'''
        return self._song_dict['header_image_thumbnail_url']

    @property
    def header_image_url(self):
        '''URL for the song's header image (1000x1000) -> str'''
        return self._song_dict['header_image_url']

    @property
    def lyrics_owner(self):
        '''ID of lyrics owner -> str'''
        return self._song_dict['lyrics_owner_id']

    @property
    def path(self):
        '''
        Return path after the top-level domain -> str

        Generally: '{Primary artist name}-{song title}-lyrics'
        e.g. '/Kendrick-lamar-the-blacker-the-berry-lyrics'
        '''
        return self._song_dict['path']

    @property
    def pyongs_count(self):
        '''Return number of pyongs on song -> int'''
        return self._song_dict['pyongs_count']

    @property
    def recording_location(self):
        '''Return recording location of song -> str (?)'''
        return self._song_dict['recording_location']

    @property
    def release_date(self):
        '''
        Release date -> str

        e.g. '2014-03-17'
        '''
        return self._song_dict['release_date']

    @property
    def song_art_image_thumbnail_url(self):
        '''URL of song art image thumbnail (300x300) -> str'''
        return self._song_dict['song_art_image_thumbnail_url']

    @property
    def song_art_image_url(self):
        '''URL of song art image (1000x1000) -> str'''
        return self._song_dict['song_art_image_url']

    @property
    def stats(self):
        '''
        Song stats -> dict

        Keys:
        accepted_annotations -> int
        concurrents -> int
        hot -> bool
        iq_earners -> int
        pageviews -> int
        trascribers -> int
        unreviewed_annotations -> int
        verified_annotations -> int
        '''
        return self._song_dict['stats']

    @property
    def title(self):
        '''Song title -> str'''
        return self._song_dict['title']

    @property
    def url(self):
        '''Full Genius web URL of song -> str'''
        return 'https://genius.com' + self._song_dict['path']

    def __repr__(self):
        '''
        TODO: should probably separate full API response and the object's response
        '''
        return json.dumps(self.resp_json)
