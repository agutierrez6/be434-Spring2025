#!/usr/bin/env python3
"""
Author : Abraham Gutierrez <agutierrez6@arizona.edu>
Date   : 2025-01-29
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Greetings and howdy",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-g",
        "--greeting",
        help="The greeting",
        metavar="str",
        type=str,
        default="Howdy",
    )

    parser.add_argument(
        "-n",
        "--name",
        help="Whom to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

    parser.add_argument(
        "-e",
        "--excited",
        help="Add an exclamation point",
        action="store_true",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    greeting = (
        f"{args.greeting}, {args.name}! "
        if args.excited
        else f"{args.greeting}, {args.name}."
    )

    print(greeting)


# --------------------------------------------------
if __name__ == "__main__":
    main()
