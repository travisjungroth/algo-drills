"""
ID: c21a2061-17de-4b06-b8de-f124ef2cf564
https://leetcode.com/problems/leaf-similar-trees/
"""
from src.typehints import Node
from itertools import zip_longest


def leaf_similar(root1: Node, root2: Node) -> bool:
    """
    Consider all the leaves of a binary tree, from left to right order,
    the values of those leaves form a leaf value sequence.
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
    """
    def dfs(root):
        if root is None:
            return
        if root.left is None and root.right is None:
            yield root.val
        yield from dfs(root.left)
        yield from dfs(root.right)
    return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))
