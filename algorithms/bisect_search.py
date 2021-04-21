"""
ID: d5c1e52d-602a-4c27-a39f-2b53caff987d
https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
"""
from collections.abc import Callable


def bisect_search(condition: Callable[[int], bool], lower: int, upper: int) -> int:
    """Find the lowest int between lower and upper where condition(int) is True."""
    left, right = lower, upper
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
