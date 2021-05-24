"""
ID: 88bad34a-271e-4096-9036-6bda1cbd4fc0
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
"""
from collections.abc import Mapping, Set
from typing import Optional

from src.typehints import Node


def dfs_component_dict_recur(
    graph: Mapping[Node, Set[Node]],
    start: Node,
    component: Optional[Set[Node]] = None
) -> set[Node]:
    """Recursively find all the nodes connected to start."""
    if component is None:
        component = set()
    component.add(start)
    for new_node in graph[start] - component:
        dfs_component_dict_recur(graph, new_node, component)
    return component
