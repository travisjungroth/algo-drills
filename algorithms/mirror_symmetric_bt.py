"""
ID: 90e4257a-ccb8-4907-b3cd-e20cd123ec40
https://leetcode.com/problems/symmetric-tree/
"""
from src.typehints import Node


def mirror_symmetric_bt(root: Node) -> bool:
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """
    return root is None or validator(root.left, root.right)


def validator(left: Node, right: Node) -> bool:
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return validator(left.left, right.right) and validator(left.right, right.left)
