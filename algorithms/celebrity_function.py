"""
834cdcc9-ff3e-497c-884e-8bf6a93a90c1
Python Algorithms, page 80
"""
from collections.abc import Callable
from typing import Optional


def celebrity_function(knows: Callable[[int, int], bool], n: int) -> Optional[int]:
    candidate = 0
    for node in range(1, n):
        if knows(candidate, node):
            candidate = node
    if any(knows(candidate, node) for node in range(candidate)):
        return None
    if any(not knows(node, candidate) for node in range(n)):
        return None
    return candidate
