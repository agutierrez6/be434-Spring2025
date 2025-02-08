#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-02-05
Purpose: Divide two required integer values
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Divide two integer values",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("num1", metavar="INT", type=int, help="First number")

    parser.add_argument("num2", metavar="INT", type=int, help="Second number")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num1 = args.num1
    num2 = args.num2

    if num2 == 0:
        print("usage: Cannot divide by zero, dum-dum!", file=sys.stderr)
        sys.exit(1)
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {int(result)}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
