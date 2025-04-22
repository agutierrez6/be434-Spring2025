
#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-21
Purpose: FASTA sequence statistics
"""

import argparse
import os
import sys
from tabulate import tabulate


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print sequence stats',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        nargs='+',
                        help='Input FASTA file(s)',
                        metavar='FILE')

    parser.add_argument('-t', '--tablefmt',
                        help='Tabulate table style',
                        metavar='table',
                        default='plain')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    
    table = []
    for file in args.FILE:
        if not os.path.isfile(file):
            parser = get_args()
            parser.print_usage()
            print(f"No such file or directory: '{file}'")
            sys.exit(1)
            
        sequences = []
        with open(file) as fh:
            current_seq = ''
            for line in fh:
                if line.startswith('>'):
                    if current_seq:
                        sequences.append(current_seq)
                    current_seq = ''
                else:
                    current_seq += line.strip()
            if current_seq:
                sequences.append(current_seq)

        num_seqs = len(sequences)
        min_len = min([len(s) for s in sequences]) if sequences else 0
        max_len = max([len(s) for s in sequences]) if sequences else 0
        avg_len = sum([len(s) for s in sequences])/num_seqs if sequences else 0
        
        table.append([file, min_len, max_len, f'{avg_len:.2f}', num_seqs])

    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    print(tabulate(table, headers=headers, tablefmt=args.tablefmt))


if __name__ == '__main__':
    main()
