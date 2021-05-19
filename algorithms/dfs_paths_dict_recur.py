"""
ID: 3df740e0-34f3-4852-add2-7076c8be47c3
"""
from collections.abc import Iterable, Mapping
from typing import Optional

from src.typehints import Node


def dfs_paths_dict_recur(
    graph: Mapping[Node, set[Node]],
    start: Node,
    goal: Node,
    path: Optional[list[Node]] = None
) -> Iterable[list[Node]]:
    """Find all the paths from start to goal recursively on a dict."""
    if path is None:
        path = [start]
    if start == goal:
        yield path
    else:
        for next_node in graph[start].difference(path):
            next_path = path + [next_node]
            yield from dfs_paths_dict_recur(graph, next_node, goal, next_path)
