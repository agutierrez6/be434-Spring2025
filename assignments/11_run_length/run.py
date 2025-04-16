#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-15
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Run-length encoding/data compression",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("positional", metavar="str", help="DNA text or file")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    if os.path.isfile(args.positional):
        with open(args.positional, encoding='utf-8') as fh:
            text = fh.read().strip()
    else:
        text = args.positional
    for seq in text.splitlines():
        print(rle(seq))


def rle(seq):
    """Return run-length encoding of seq"""
    if not seq:
        return ""
    result = ""
    count = 1
    current = seq[0]
    for char in seq[1:]:
        if char == current:
            count += 1
        else:
            result += current + (str(count) if count > 1 else "")
            current = char
            count = 1
    result += current + (str(count) if count > 1 else "")
    return result


def test_rle():
    """Test run-length encoding"""
    assert rle("A") == "A"
    assert rle("ACGT") == "ACGT"
    assert rle("AA") == "A2"
    assert rle("AAAAA") == "A5"
    assert rle("ACCGGGTTTT") == "AC2G3T4"


# --------------------------------------------------
if __name__ == "__main__":
    main()
