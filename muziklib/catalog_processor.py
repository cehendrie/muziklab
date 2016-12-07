__author__ = 'chendrie'

import file_object
import entry


class CatalogProcessor(object):

    def __init__(self, filepath='.', filename='samplecat.txt'):
        self.filepath = filepath
        self.filename = filename

    def generate_entries(self):
        lines = self.read_file()
        entries = []
        for line in lines:
            #print line
            entries.append(self.build_entry(line))
        return entries

    def read_file(self):
        fo = file_object.FileObject(self.filepath, self.filename)
        lines = fo.file.readlines()
        return lines

    def build_entry(self, line):
        line = line.strip()
        tokens = line.split("|")
        e = entry.Entry(tokens[0], tokens[1], tokens[2], tokens[3], line)
        return e
