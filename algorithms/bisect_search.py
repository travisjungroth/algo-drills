"""
d5c1e52d-602a-4c27-a39f-2b53caff987d
"""
from collections.abc import Callable


def bisect_search(condition: Callable[[int], bool], lower: int, upper: int) -> int:
    left, right = lower, upper
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
