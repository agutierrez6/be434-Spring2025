#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-28
Purpose: Caesar shift
"""

import argparse
import sys
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Caesar shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
         "positional",
         metavar="FILE",
         help="Input file",
         type=argparse.FileType("rt"),
    )
    parser.add_argument(
        "-n",
        "--number",
        help="A number to shift",
        metavar="NUMBER",
        type=int,
        default=3,
    )
    parser.add_argument(
        "-d",
        "--decode",
        help="A boolean flag",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    shift = args.number % 26
    if args.decode:
        shift = -shift
    alpha = string.ascii_uppercase
    trans = alpha[shift:] + alpha[:shift]
    table = str.maketrans(alpha, trans)
    lines = [line.rstrip("\n") for line in args.positional]
    translated = [text.upper().translate(table) for text in lines]
    out_fh = args.outfile or sys.stdout
    out_fh.write("\n".join(translated))


# --------------------------------------------------
if __name__ == "__main__":
    main()
