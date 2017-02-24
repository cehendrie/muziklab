"""
core

A process script to read a file of album information and sort by band and release year
"""

import os
from operator import attrgetter
from argparse import ArgumentParser
from library import Library


def build_argparse():
    """
    Build a command line parser.
    """
    cli = ArgumentParser()
    cli.add_argument('--path',
                     required=True,
                     help='a path to the file representing a music library')
    cli.add_argument('--test',
                     action='store_true',
                     help='a flag for validating a single file')
    return cli


def get_filepaths(path):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []
    if os.path.isfile(path):
        file_paths.append(path)
    else:
        for root, _, files in os.walk(path):
            for filename in files:
                if filename.startswith(".") is False:
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)  # Add it to the list.
    return file_paths


def main():
    """
    The core entry point.
    """
    cli = build_argparse()
    args = cli.parse_args()

    files = get_filepaths(args.path)

    if args.test is False:
        library = Library(files)
        entries = library.load()
        entries = sorted(entries, key=attrgetter('artist', 'year'))
        for entry in entries:
            print(entry.raw)
    else:
        if len(files) > 1:
            print("[Error] unable to test multiple files: {0}".format(len(files)))
            exit(1)
        else:
            library = Library(files)
            error = library.validate()
            if len(error) > 0:
                print("[Error] invalid file")

    exit(0)


if __name__ == '__main__':
    main()
