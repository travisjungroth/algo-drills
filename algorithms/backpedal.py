"""
ebd60a5b-403f-4eac-a651-8a9a52c2b11c
"""
from collections.abc import Mapping
from typing import Optional

from hints import Node


def backpedal(goal: Node, parents: Mapping[Node, Optional[Node]]) -> list[Node]:
    back_path = []
    node = goal
    while node is not None:
        back_path.append(node)
        node = parents[node]
    return back_path[::-1]
