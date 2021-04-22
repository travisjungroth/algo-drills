"""
ID: de877076-d103-430f-946c-08a82aa6a576
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
"""
from collections import deque
from collections.abc import Iterable, Mapping

from hints import Node


def bfs_paths_dict(graph: Mapping[Node, set[Node]], start: Node, goal: Node) -> Iterable[list[Node]]:
    """Find all the paths from start to goal using BFS on a dict."""
    to_visit = deque([[start]])
    while to_visit:
        path = to_visit.popleft()
        node = path[-1]
        if node == goal:
            yield path
        else:
            for next_node in graph[node].difference(path):
                to_visit.append(path + [next_node])
