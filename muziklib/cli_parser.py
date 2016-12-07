__author__ = 'chendrie'

"""
cli

http://docs.python.org/2/library/argparse.html#module-argparse
http://mancoosi.org/~abate/command-line-parsing-python
"""

import argparse


class CliParser(object):

    """
    A simple wrapper for the argparse parser.
    """

    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description)

    def retrieve_parser(self):
        self.parser.add_argument('-p', '--filepath', required=True)
        self.parser.add_argument('-f', '--filename', required=True)
        self.parser.add_argument('-c', '--config', default='false')
        return self.parser

    def __str__(self):
        return "usage: %s" % (self.parser.print_help())
