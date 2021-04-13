"""Python Algorithms, page 80"""
from collections.abc import Callable
from typing import Optional


def celebrity_function(knows: Callable[[int, int], bool], n: int) -> Optional[int]:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    if any(knows(candidate, i) for i in range(candidate)):
        return None
    if any(not knows(i, candidate) for i in range(n)):
        return None
    return candidate
