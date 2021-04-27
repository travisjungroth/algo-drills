"""
ID: 0ff2f1b7-0112-4990-8897-b05c2cdbcbca
Python Algorithms, Page 102
"""

from collections import deque
from collections.abc import Iterable, Mapping, Set

from hints import Node


def bfs_component_dict(graph: Mapping[Node, Set[Node]], start: Node) -> Iterable[Node]:
    """Find all the nodes connected to the starting node, using BFS on a dict."""
    component = set()
    to_visit = deque([start])
    while to_visit:
        node = to_visit.popleft()
        if node in component:
            continue
        component.add(node)
        to_visit.extend(graph[node])
        yield node
