"""
1288e78d-bc7a-44da-8774-41c0e4dcfe70
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
from collections.abc import Mapping
from math import inf
from numbers import Rational

from hints import Node


def dijkstras_distances_min(graph: Mapping[Node, Mapping[Node, Rational]], start: Node) -> dict[Node: Rational]:
    distances = dict.fromkeys(graph, inf)
    distances[start] = 0
    unvisited = set(graph)
    while unvisited:
        node = min(unvisited, key=distances.__getitem__)
        unvisited.remove(node)
        distance = distances[node]
        for next_node, weight in graph[node].items():
            next_distance = distance + weight
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
    return distances
