"""
ID: c1810bc6-753a-44ce-aae3-56ec13b089d1
https://leetcode.com/problems/binary-tree-paths/
"""
from src.typehints import Node


def bt_paths(root: Node) -> list[str]:
    """
    Given the root of a binary tree, return all root-to-leaf paths in any order.
    A leaf is a node with no children.
    """
    node_path = [(root, "")]
    paths = []
    while node_path:
        node, path = node_path.pop()
        if not node.left and not node.right:
            paths.append(f'{path}{str(node.val)}')
        if node.left:
            node_path.append((node.left, f'{path}{str(node.val)}->'))
        if node.right:
            node_path.append((node.right, f'{path}{str(node.val)}->'))
    return paths
