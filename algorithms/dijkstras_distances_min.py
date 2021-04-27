"""
ID: 1288e78d-bc7a-44da-8774-41c0e4dcfe70
Grokking Algorithms, Page 115
Python Algorithms, Page 194
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

The explanation in Grokking Algorithms is good, but the code is needlessly complicated.
This is a minimalist Dijkstras. See the other versions for more features and better time complexity.
"""
from collections.abc import Mapping
from math import inf
from numbers import Rational

from hints import Node


def dijkstras_distances_min(graph: Mapping[Node, Mapping[Node, Rational]], start: Node) -> dict[Node: Rational]:
    """Find the minimum distance from start to all connected nodes on a directed, weighted graph."""
    distances = dict.fromkeys(graph, inf)
    distances[start] = 0
    unvisited = set(graph)
    while unvisited:
        # Using min like this increases the time complexity compared to a priority queue, but it simplifies things.
        node = min(unvisited, key=distances.__getitem__)
        unvisited.remove(node)
        distance = distances[node]
        for next_node, weight in graph[node].items():
            distances[next_node] = min(distance + weight, distances[next_node])
    return distances
