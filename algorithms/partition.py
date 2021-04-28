"""
ID: 2f71a85e-3c15-404c-ad79-1bbe24890762
https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
Python Algorithms, Page 123

This partition function is useful to quickselect and quicksort. There are other partition algorithms you can
pass into those algorithms for different performance.
"""
from collections.abc import Sequence

from typehints import T


def partition(seq: Sequence[T]) -> tuple[list[T], T, list[T]]:
    """Split sequence into a tuple of lesser or equal values, first value, greater values."""
    pivot, *rest = seq
    low = [n for n in rest if n <= pivot]
    high = [n for n in rest if n > pivot]
    return low, pivot, high
