#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-02-26
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Transcribe DNA to RNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE", nargs="+", help="Input DNA file(s)")

    parser.add_argument(
        "-o",
        "--out_dir",
        help="Output directory",
        metavar="DIR",
        type=str,
        default="out",
    )

    return parser


# --------------------------------------------------
def main():
    """Main function to transcribe DNA to RNA"""

    parser = get_args()
    args = parser.parse_args()

    if not isinstance(args.out_dir, str):
        sys.exit("Error: Output directory must be a string.")

    if not os.path.exists(args.out_dir):
        try:
            os.makedirs(args.out_dir, exist_ok=True)
        except OSError as e:
            sys.stderr.write(f"Error creating output directory: {e}\n")
            sys.exit(1)

    processed_sequences = 0
    processed_files = 0

    for file in args.FILE:
        if not os.path.exists(file):
            parser.print_usage(sys.stderr)
            sys.stderr.write(f"No such file or directory: '{file}'\n")
            sys.exit(1)

        try:
            with open(file, "r", encoding="utf-8") as f:
                dna_seq_list = [line.strip() for line in f.readlines() if line.strip()]

            if not dna_seq_list:
                sys.stderr.write(f"Warning: File '{file}' is empty.\n")

            out_file = os.path.join(args.out_dir, os.path.basename(file))

            with open(out_file, "w", encoding="utf-8") as out_f:
                rna_sequences = [
                    dna_seq.replace("T", "U").replace("t", "u")
                    for dna_seq in dna_seq_list
                ]

                out_f.write("\n".join(rna_sequences) + "\n")

            processed_sequences += len(rna_sequences)
            processed_files += 1

        except (FileNotFoundError, IOError) as e:
            sys.stderr.write(f"Error reading or processing file {file}: {e}\n")
            sys.exit(1)

    sequence_word = "sequence" if processed_sequences == 1 else "sequences"
    file_word = "file" if processed_files == 1 else "files"

    print(
        f"Done, wrote {processed_sequences} {sequence_word} in"
        f' {processed_files} {file_word} to directory "{args.out_dir}".'
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
