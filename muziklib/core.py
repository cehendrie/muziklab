"""
core
- a process script to read a file of album information and sort by band and release year

TODO
1. add command line parsing
2. move inline classes to individual files
2. allow music catalog file to be define on the command line
3. allow multiple music catalog files be entered via config file
4. determine various artists albums and sort various artist within file
5. add format type to sort (possibly hierarchy of types)
6. dynamically determine album input tokens
"""

from operator import attrgetter
from argparse import ArgumentParser
from library import Library


def build_argparse():

    cli = ArgumentParser()
    cli.add_argument('--path',
                     required=True,
                     help='a path to the file representing a music library')
    return cli

def main():

    cli = build_argparse()
    args = cli.parse_args()

    library = Library([args.path])
    entries = library.load()
    entries = sorted(entries, key=attrgetter('artist', 'year'))

    for entry in entries:
        print(entry.raw)

if __name__ == '__main__':
    main()
