"""
ID: 6e122846-ff51-47ba-bf8a-e8d04dbdac3b
https://leetcode.com/problems/binary-tree-level-order-traversal/

The essential thing about level order traversal is the inner for loop over the length of the level.
Above that loop is where you can do any per-level operations. In this case, yielding a copy of the level.
You can use a stack instead of a queue by copying and replacing it on each level.
"""
from collections import deque
from typing import Iterable

from src.typehints import BTNode


def bt_level_order_traversal_iter(root: BTNode) -> Iterable[list[BTNode]]:
    # would do a null check here if root was Optional
    level = deque([root])
    while level:
        # modify this line if you needed to grab the values
        yield list(level)  # copy so it's not messed with
        for _ in range(len(level)):
            node = level.pop()
            for child in [node.right, node.left]:
                if child is not None:
                    level.appendleft(child)
