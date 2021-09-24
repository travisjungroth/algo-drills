"""
ID: b84ce758-8dfd-40c8-92a8-cb15b26dfdac
https://leetcode.com/problems/binary-tree-tilt/
"""
from src.typehints import Node


def bt_tilt(root: Node) -> int:
    """
    Given the root of a binary tree, return the sum of every tree node's tilt.
    The tilt of a tree node is the absolute difference between the sum of
    all left subtree node values and all right subtree node values.
    If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
    The rule is similar if there the node does not have a right child.
    """
    def tilt(node):
        if not node:
            return 0, 0
        left = tilt(node.left)
        right = tilt(node.right)
        return left[0] + right[0] + node.val, abs(left[0] - right[0]) + left[1] + right[1]
    return tilt(root)[1]
