#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-02-15
Purpose: Count tetranuclotide frequency in a DNA sequence
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        help='Input DNA sequence')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.DNA.upper()
    counts = [dna.count(base) for base in ['A', 'C', 'G', 'T']]
    print(''.join(map(str, counts)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
