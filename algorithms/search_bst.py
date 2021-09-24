"""
ID: 6ed7cf68-2955-4acd-941b-1717ab5de42b
https://leetcode.com/problems/search-in-a-binary-search-tree/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
from typing import Optional

from src.typehints import Node


def search_bst(root: Node, val: int) -> Optional[Node]:
    """
    You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST with val equal to val and return the subtree rooted with that node.
    If such a node does not exist, return None.
    """
    to_visit = [root]
    while to_visit:
        node = to_visit.pop()
        if node is not None:
            if node.val > val:
                to_visit.append(node.left)
            elif node.val < val:
                to_visit.append(node.right)
            else:
                return node
