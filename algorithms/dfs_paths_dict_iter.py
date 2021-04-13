from collections.abc import Iterable, Mapping

from hints import Node


def dfs_paths_dict_iter(graph: Mapping[Node, set[Node]], start: Node, goal: Node) -> Iterable[list[Node]]:
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            yield path
            continue
        for next_node in graph[node].difference(path):
            next_path = path + [next_node]
            stack.append(next_path)
