from __future__ import annotations
import argparse
from censearch import VERSION


def parse_args() -> argparse.Namespace:
    """:"""
    parser = argparse.ArgumentParser()
    main_args = parser.add_argument_group()

    main_args.add_argument("-o", "--output", help="output results to a file", type=str)
    main_args.add_argument(
        "-s", "--search", help="phrase to search", type=str, required=True
    )
    main_args.add_argument(
        "--version",
        help="print version info",
        version=f"censearch.py {VERSION}",
        action="version",
    )
    # main_args.add_argument("-u", "--user", help="username to search", type=str)
    return parser.parse_args()
