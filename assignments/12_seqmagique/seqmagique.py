#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-21
Purpose: Argparse Python script
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t', '--tablefmt',
                        metavar='table',
                        help='Tabulate table style',
                        default='plain')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    table = []  # Initialize the table as an empty list

    lengths = []
    for file in args.FILE:
        try:
            with open(file) as fh:
                lengths = [
                    len(seq)
                    for seq in (
                        s.strip().split('\n', 1)[1].replace('\n', '')
                        for s in fh.read().split('>')
                        if s and '\n' in s
                    )
                ]
        except FileNotFoundError:
            sys.exit(f"No such file or directory: '{file}'")

        lengths = lengths if 'lengths' in locals() else []

        num = len(lengths)
        minlen = min(lengths) if lengths else 0
        maxlen = max(lengths) if lengths else 0
        avglen = sum(lengths) / num if num else 0
        table.append([file, minlen, maxlen, f'{avglen:.2f}', num])

    try:
        from tabulate import tabulate
    except ImportError:
        sys.exit("This program requires 'tabulate' module. Try: pip install tabulate")

    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    print(tabulate(table, headers=headers, tablefmt=args.tablefmt))


# --------------------------------------------------
if __name__ == '__main__':
    main()
