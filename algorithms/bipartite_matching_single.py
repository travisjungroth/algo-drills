"""
ID: 916cdf1e-c509-4dfe-bdee-fef5ad30798a
Python Algorithms, Page 78
"""
from collections.abc import Sequence


def bipartite_matching_single(graph: Sequence[int]) -> list[int]:
    matches = list(graph)
    in_degrees = [0] * len(graph)  # This is an alternate to collections.Counter when the keys are 0-n.
    for target in graph:
        in_degrees[target] += 1
    zero_in_degrees = [node for node, in_degree in enumerate(in_degrees) if not in_degree]
    while zero_in_degrees:
        node = zero_in_degrees.pop()
        target = matches[node]
        matches[node] = node
        in_degrees[target] -= 1
        if not in_degrees[target]:
            zero_in_degrees.append(target)
    return matches
