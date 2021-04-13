from collections import deque
from collections.abc import Iterable, Mapping

from hints import Node


def bfs_paths_dict_iter(graph: Mapping[Node, set[Node]], start: Node, goal: Node) -> Iterable[list[Node]]:
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            yield path
        else:
            for next_node in graph[node].difference(path):
                next_path = path + [next_node]
                queue.append(next_path)
