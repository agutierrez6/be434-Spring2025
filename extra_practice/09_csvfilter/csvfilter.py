#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-04-03
Purpose: Filter delimited records
"""

import argparse
import csv
import re
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Filter delimited records",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        required=True,
    )

    parser.add_argument(
        "-v",
        "--val",
        help="Value for filter",
        metavar="val",
        required=True,
    )

    parser.add_argument(
        "-c",
        "--col",
        help="Column name for filter",
        metavar="col",
        default="",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="OUTFILE",
        default="out.csv",
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        help="Input delimiter",
        metavar="delim",
        default=",",
    )

    return parser.parse_args()


def main():
    """Filter records and write matching rows to the output file"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if args.col and args.col not in reader.fieldnames:
        sys.stderr.write(f'--col "{args.col}" not a valid column!\n')
        valid_fields = (
            ", ".join(reader.fieldnames)
            if reader.fieldnames
            else "No headers found"
        )
        sys.stderr.write(f"Choose from {valid_fields}\n")
        sys.exit(1)

    with open(args.outfile, "wt", newline="", encoding="utf-8") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        count = 0
        pattern = re.compile(re.escape(args.val), re.IGNORECASE)

        for row in reader:
            if args.col:
                field_value = row.get(args.col, "")
                if pattern.search(field_value):
                    writer.writerow(row)
                    count += 1
            else:
                if any(pattern.search(str(val)) for val in row.values()):
                    writer.writerow(row)
                    count += 1

    print(f'Done, wrote {count} to "{args.outfile}".')


if __name__ == "__main__":
    main()
