"""
ID: c4daa80d-e471-4223-b4e6-e9baed5e4aed
Python Algorithms, Page 82

Cyclic graph will return the nodes that can be sorted.
"""
from collections import Counter
from collections.abc import Iterable, Mapping
from itertools import chain

from hints import Node


def topo_sort_count(graph: Mapping[Node, Iterable]) -> Iterable[Node]:
    """Find a topological sorting of a graph by counting in-degrees."""
    in_degrees = Counter(chain(*graph.values()))
    zero_in_degrees = [node for node in graph if not in_degrees[node]]
    while zero_in_degrees:
        node = zero_in_degrees.pop()
        yield node
        for next_node in graph[node]:
            in_degrees[next_node] -= 1
            if not in_degrees[next_node]:
                zero_in_degrees.append(next_node)
