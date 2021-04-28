"""
ID: a44325d3-9846-4032-b443-04fd5a5ebddf
Python Algorithms, Page 123
"""
from collections.abc import Sequence

from algorithms.partition import partition
from typehints import T


def quickselect(seq: Sequence[T], k: int) -> T:
    """Find the kth smallest item in a sequence."""
    low, pivot, high = partition(seq)
    low_len = len(low)
    if low_len == k:
        return pivot
    elif low_len < k:
        return quickselect(high, k - low_len - 1)
    else:
        return quickselect(low, k)
