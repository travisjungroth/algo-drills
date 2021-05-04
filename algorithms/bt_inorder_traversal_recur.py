"""
ID: b9cd1e0a-a238-44a7-8116-8ae959d38f29
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from collections.abc import Iterable
from typing import Optional

from src.typehints import BTNode


def bt_inorder_traversal_recur(root: Optional[BTNode]) -> Iterable[BTNode]:
    if root is not None:
        yield from bt_inorder_traversal_recur(root.left)
        yield root.val
        yield from bt_inorder_traversal_recur(root.right)
