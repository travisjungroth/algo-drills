"""
ID: 0ff2f1b7-0112-4990-8897-b05c2cdbcbca
"""

from collections.abc import Iterable, Mapping, Set

from src.typehints import Node


def dfs_component_dict(graph: Mapping[Node, Set[Node]], start: Node) -> Iterable[Node]:
    """Find all the nodes connected to the starting node, using DFS on a dict."""
    component = {start}
    to_visit = [start]
    while to_visit:
        node = to_visit.pop()
        new_nodes = graph[node] - component
        to_visit.extend(new_nodes)
        component |= new_nodes
        yield node
