#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-08
Purpose: Find conserved bases
"""

import argparse
import sys
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find conserved bases",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE",
        metavar="FILE",
        help="Input file",
        type=argparse.FileType("rt"),
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = read_seqs(args.FILE)

    if not seqs:
        print("No sequences found", file=sys.stderr)
        sys.exit(1)

    lengths = set(map(len, seqs))
    if len(lengths) > 1:
        print("Sequences are not the same length", file=sys.stderr)
        sys.exit(1)

    for seq in seqs:
        print(seq)

    print(find_conserved(seqs))


def read_seqs(file) -> List[str]:
    """Read sequences from file"""
    sequences = [line.strip() for line in file if line.strip()]
    return sequences


def find_conserved(seqs: List[str]) -> str:
    """Find conserved bases"""
    if not seqs:
        return ''

    length = len(seqs[0])
    conserved = []

    for i in range(length):
        bases = [seq[i] for seq in seqs]
        conserved.append('|' if all(b == bases[0] for b in bases) else 'X')

    return ''.join(conserved)


# --------------------------------------------------
if __name__ == "__main__":
    main()
