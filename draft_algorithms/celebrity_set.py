from collections.abc import Mapping, Set
from typing import Optional

from hints import Node


def celebrity_set(graph: Mapping[Node, Set[Node]]) -> Optional[Node]:
    """Seems not more useful than the function version."""
    candidate = next(iter(graph))
    for node in graph:
        if node in graph[candidate]:
            candidate = node
    if not graph[candidate] and all(candidate in adjacent or candidate == node for node, adjacent in graph.items()):
        return candidate
    return None
