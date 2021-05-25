"""
ID: 4d4a5521-ebd2-4f8c-95a3-ef67db3aeecf
https://leetcode.com/problems/balance-a-binary-search-tree/
"""
from collections.abc import Sequence
from typing import Optional

from src.typehints import BTNode


def bst_make_balanced_recur(values: Sequence[int]) -> Optional[BTNode]:
    """Make a balanced binary search tree from a sorted sequence of values."""
    if not values:
        return None
    mid = len(values) // 2
    root = BTNode(values[mid])
    root.left = bst_make_balanced_recur(values[:mid])
    root.right = bst_make_balanced_recur(values[mid + 1:])
    return root
