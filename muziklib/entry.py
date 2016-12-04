__author__ = 'chendrie'


class Entry:

    """
    A container to hold one music catalog entry.
    """

    def __init__(self, artist, album, year, format_type, raw):

        self.artist = artist
        self.album = album
        self.year = year
        self.format_type = format_type
        self.raw = raw

    def __str__(self):
        return "Entry [artist: %s, album: %s, year: %s, format: %s]" % (self.artist, self.album, self.year, self.format_type)
