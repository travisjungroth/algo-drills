from collections.abc import Mapping, Set
from typing import Optional

from hints import Node


def dfs_component_dict_recur(
    graph: Mapping[Node, Set[Node]],
    start: Node,
    component: Optional[Set[Node]] = None
) -> set[Node]:
    if component is None:
        component = set()
    component.add(start)
    for next_node in graph[start] - component:
        dfs_component_dict_recur(graph, next_node, component)
    return component
