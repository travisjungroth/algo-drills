"""
ID: b2c5ac2f-bec2-4e37-a6df-35672faabf9f
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from src.typehints import BTNode
from typing import Optional, Sequence


def make_balanced_bst(values: Sequence[int], start=0, stop=None) -> Optional[BTNode]:
    """
    Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth
    of the two subtrees of every node never differs by more than one.
    """
    if stop is None:
        stop = len(values)
    if start == stop:
        return None
    mid = (stop + start) // 2
    root = BTNode(values[mid])
    root.left = make_balanced_bst(values, start=start, stop=mid)
    root.right = make_balanced_bst(values, start=mid + 1, stop=stop)
    return root
