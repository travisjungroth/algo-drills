from collections import deque
from collections.abc import Mapping, Set

from hints import Node


def bfs_component_dict_iter(graph: Mapping[Node, Set[Node]], start: Node) -> set[Node]:
    component = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visit = graph[node] - component
        component |= visit
        queue.extend(visit)
    return component
