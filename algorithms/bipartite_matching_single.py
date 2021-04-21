"""
916cdf1e-c509-4dfe-bdee-fef5ad30798a
Python Algorithms, page 78
"""
from collections.abc import Sequence


def bipartite_matching_single(graph: Sequence[int]) -> list[int]:
    matches = list(graph)
    in_degrees = [0] * len(graph)
    for node in graph:
        in_degrees[node] += 1
    zero_in_degrees = [node for node, count in enumerate(in_degrees) if not count]
    while zero_in_degrees:
        node = zero_in_degrees.pop()
        outgoing = matches[node]
        matches[node] = node
        in_degrees[outgoing] -= 1
        if not in_degrees[outgoing]:
            zero_in_degrees.append(outgoing)
    return matches
