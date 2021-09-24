"""
ID: 45bf62b9-7813-4bf7-96ec-9be00da84a46
"""
import math
from src.typehints import BTNode


def valid_bst(root: BTNode, left=-math.inf, right=math.inf):
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    """
    return not root or left < root.val < right and \
        valid_bst(root=root.left, left=left, right=root.val) and \
        valid_bst(root=root.right, left=root.val, right=right)
