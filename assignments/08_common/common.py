#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-03-24
Purpose: Find common words in two files
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words in two files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file1",
        metavar="FILE1",
        type=argparse.FileType("r"),
        help="Input file 1"
    )

    parser.add_argument(
        "file2",
        metavar="FILE2",
        type=argparse.FileType("r"),
        help="Input file 2"
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words1 = set(args.file1.read().split())
    words2 = set(args.file2.read().split())

    common = sorted(words1.intersection(words2))

    for word in common:
        print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
