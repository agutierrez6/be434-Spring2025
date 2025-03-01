#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-02-27
Purpose: Compute GC content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Compute GC content",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="?",
        type=argparse.FileType("rt"),
        default=sys.stdin,
        help="Input sequence file",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequences = {}
    seq_id = None

    with args.file as fh:
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                seq_id = line[1:]
                sequences[seq_id] = []
            elif seq_id:
                sequences[seq_id].append(line)

    best_seq = None
    highest_gc = -1.0

    for seq_id, seq_lines in sequences.items():
        full_sequence = "".join(seq_lines)
        total_count = len(full_sequence)

        if total_count > 0:
            gc_count = sum(1 for base in full_sequence if base in "GC")
            gc_content = (gc_count / total_count) * 100

            if gc_content > highest_gc:
                highest_gc = gc_content
                best_seq = seq_id

    if best_seq:
        print(f"{best_seq} {highest_gc:.6f}")
    else:
        print("No valid sequence found")


# --------------------------------------------------
if __name__ == "__main__":
    main()
