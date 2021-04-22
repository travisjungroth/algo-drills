"""
ID: d5c1e52d-602a-4c27-a39f-2b53caff987d
https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
"""
from collections.abc import Callable


def bisect_search(condition: Callable[[int], bool], low: int, high: int) -> int:
    """Find the lowest int between low and high where condition(int) is True."""
    while low < high:
        mid = low + (high - low) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low
