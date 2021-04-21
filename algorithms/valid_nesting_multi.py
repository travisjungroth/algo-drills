"""
b4f4727c-8b42-4c52-b3e0-306c6191e435
"""
from collections.abc import Mapping, Sequence

from hints import Node


def valid_nesting_multi(items: Sequence[Node], openers_to_closers: Mapping[Node, Node]) -> bool:
    openers = openers_to_closers.keys()
    closers = set(openers_to_closers.values())
    unmatched_openers = []
    for item in items:
        if item in openers:
            unmatched_openers.append(item)
        elif item in closers:
            if not unmatched_openers:
                return False
            unmatched_opener = unmatched_openers.pop()
            expected_closer = openers_to_closers[unmatched_opener]
            if item != expected_closer:
                return False
    return not unmatched_openers
