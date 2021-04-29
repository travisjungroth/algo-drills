#!/usr/bin/env python3
import argparse

from src.commands import new_algo, practice, search_reference

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()
    # practice
    parser_practice = sub_parser.add_parser(
        'practice',
        description='Practice your algorithms in workspace.py',
        help='Practice your algorithms in workspace.py',
    )
    parser_practice.add_argument('algo', help='The name or UUID of the algo to advance to after completion.', nargs='?')
    parser_practice.set_defaults(func=practice)
    # search_reference
    parser_reference = sub_parser.add_parser(
        'search_reference',
        description='Search for algorithms by reference.',
        help='Search for algorithms by reference.',
    )
    parser_reference.add_argument(
        'reference',
        help='The name of the reference to search for.',
        choices=['Grokking Algorithms', 'Python Algorithms'],
    )
    parser_reference.add_argument(
        '-n',
        '--new',
        action='store_true',
        help="Only show algorithms that aren't yet allowed."
    )
    parser_reference.set_defaults(func=search_reference)
    # new_algo
    parser_search = sub_parser.add_parser(
        'new_algo',
        description='Create a new empty algorithm.',
        help='Create a new empty algorithm.',
    )
    parser_search.add_argument(
        'name',
        help='Name of the function. You can change it, but keep it in sync with the file name.'
    )
    parser_search.add_argument(
        '-s',
        '--skip-allow',
        help='Skip adding it to the allow list.',
        default=False,
        action='store_false',
    )
    parser_search.set_defaults(func=new_algo)

    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    else:
        print(args.func(args))
