"""
ID: 6206d02a-7c74-40dc-a923-c4cdd503bbca
https://leetcode.com/problems/merge-two-binary-trees/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
from src.typehints import Node


def merge_two_binary_trees(root1: Node, root2: Node) -> Node:
    """Given two binary trees, return the merged tree.
    If there is a value in each tree for the same node position, use the sum of both values as the merged value.
    """
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root1.val = root1.val + root2.val
    root1.left = merge_two_binary_trees(root1.left, root2.left)
    root1.right = merge_two_binary_trees(root1.right, root2.right)
    return root1

