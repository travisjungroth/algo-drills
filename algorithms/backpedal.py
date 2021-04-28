"""
ID: ebd60a5b-403f-4eac-a651-8a9a52c2b11c

Useful with Dijkstra's when you want the path. This version assumes all the keys you need are there,
but you could use .get() instead.
"""
from collections.abc import Mapping
from typing import Optional

from typehints import Node


def backpedal(goal: Node, parents: Mapping[Node, Optional[Node]]) -> list[Node]:
    """With a dict of parent->child, walk backwards from the goal as far as possible and return the path."""
    back_path = []
    node = goal
    while node is not None:
        back_path.append(node)
        node = parents[node]
    return back_path[::-1]
