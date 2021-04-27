"""
ID: fe10d17f-e7f8-40f7-8b78-fd799cf7d4b3
Grokking Algorithms, Page 95
"""
from collections import deque
from collections.abc import Callable, Iterable, Mapping

from hints import Node


def bfs_search_dict(graph: Mapping[Node, Iterable[Node]], start: Node, predicate: Callable[[Node], bool]) -> bool:
    """Find the closest node to start that matches the predicate using breadth first search."""
    visited = set()
    to_visit = deque([start])
    while to_visit:
        node = to_visit.popleft()
        if node in visited:
            continue
        visited.add(node)
        if predicate(node):
            return True
        to_visit += graph[node]
    return False
