#!/usr/bin/env python3
import argparse

from src.commands import practice

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()
    parser_practice = sub_parser.add_parser(
        'practice',
        description='Practice your algorithms in workspace.py',
        help='Practice your algorithms in workspace.py',
    )
    parser_practice.add_argument('algo', help='The name or UUID of the algo to advance to after completion.', nargs='?')
    parser_practice.set_defaults(func=practice)
    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    else:
        print(args.func(args))
