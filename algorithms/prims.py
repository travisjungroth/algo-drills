"""
ID: c3f603f7-26a5-44d3-9295-15dab653187d

Python Algorithms, Page 153
https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""
from collections.abc import Mapping
from heapq import heappop, heappush
from typing import Optional

from src.typehints import Node


def prims(graph: Mapping[Node, Mapping[Node, int]], start: Node) -> dict[Node, Optional[Node]]:
    """Find the minimum spanning tree of an undirected, weighted graph."""
    parents = {}
    pq = [(0, None, start)]  # (weight, parent, node)
    while pq:
        _, parent, node = heappop(pq)
        if node in parents:
            continue
        parents[node] = parent
        for next_node, weight in graph[node].items():
            heappush(pq, (weight, node, next_node))
    return parents
