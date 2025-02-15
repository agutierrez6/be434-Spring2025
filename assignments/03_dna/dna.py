#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-02-15
Purpose: Accept a sequence of DNA as a single positional argument to count tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='DNA',
                        help='Input DNA sequence')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.positional
    dna = dna.upper()
    dna_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    dna = dna.replace('T', 'U')
    for base in dna:
        dna_count[base] += 1
    print(dna_count)
    print(f'DNA: {dna}')



# --------------------------------------------------
if __name__ == '__main__':
    main()
