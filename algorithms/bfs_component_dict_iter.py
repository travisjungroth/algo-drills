"""Python Algorithms, Page 102."""

from collections import deque
from collections.abc import Iterable, Mapping, Set

from hints import Node


def bfs_component_dict_iter(graph: Mapping[Node, Set[Node]], start: Node) -> Iterable[Node]:
    component = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in component:
            continue
        component.add(node)
        queue.extend(graph[node])
        yield node
