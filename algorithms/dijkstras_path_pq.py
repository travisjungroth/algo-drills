from collections.abc import Mapping
from heapq import heappop, heappush
from math import inf
from numbers import Real
from typing import Optional

from hints import Node


def dijkstras_path_pq(
    graph: Mapping[Node, Mapping[Node, Real]],
    start: Node,
    goal: Node
) -> tuple[dict[Node, Real], dict[Node, Optional[Node]]]:
    distances = dict.fromkeys(graph, inf)
    distances[start] = 0
    parents = dict.fromkeys(graph)
    unvisited = set(graph)
    pq = [(0, start)]
    while pq:
        distance, node = heappop(pq)
        if node not in unvisited:
            continue
        unvisited.remove(node)
        if node == goal:
            break
        for next_node, weight in graph[node].items():
            next_distance = distance + weight
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                parents[next_node] = node
                heappush(pq, (next_distance, next_node))
    return distances, parents
