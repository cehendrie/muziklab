"""
library.py
"""

class FileObject(object):
    """
    A simple file object.
    """

    def __init__(self, filename):
        # open a file filename in filepath in read and write mode
        self.file = open(filename, 'r+')

    def __del__(self):
        self.file.close()
        del self.file

class Entry(object):
    """
    A container to hold one music catalog entry.
    """

    def __init__(self, artist, album, year, raw):

        self.artist = artist
        self.album = album
        self.year = year
        self.raw = raw

    def __str__(self):
        return "Entry [artist: {0}, album: {1}, year: {2}]".format(self.artist, self.album, self.year)


class Library(object):
    """
    A library.
    """

    def __init__(self, files):
        self.files = files

    def load(self):

        entries = []

        for filename in self.files:
            file_object = FileObject(filename)
            lines = file_object.file.readlines()
            for line in lines:
                line = line.strip()
                tokens = line.split("|")
                entry = Entry(tokens[0],
                              tokens[1],
                              tokens[2],
                              line)
                entries.append(entry)

        return entries
