"""
ID: 14bda291-c23d-4ab0-bdf3-e0b9ee7d4faf
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from src.typehints import Node


def max_depth_bt(root: Node):
    """
    A binary tree's maximum depth is the number of nodes along
    the longest path from the root node down to the farthest leaf node.
    """
    if root is None:
        return 0
    return max(max_depth_bt(root.left), max_depth_bt(root.right)) + 1



