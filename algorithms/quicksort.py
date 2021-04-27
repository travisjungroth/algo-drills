"""
ID: 9f17b309-5ad5-4f13-81ac-814cdb8f3696
https://en.wikipedia.org/wiki/Quicksort
Grokking Algorithms, Page 60
Python Algorithms, Page 124

The partition function is split out (unlike in Grokking Algorithms) so it can be used in quickselect.
Add that to allowed.csv, also, to get the full algorithm.
"""
from collections.abc import Sequence

from algorithms.partition import partition
from hints import T


def quicksort(seq: Sequence[T]) -> list[T]:
    if len(seq) <= 1:
        return list(seq)
    low, pivot, high = partition(seq)
    return quicksort(low) + [pivot] + quicksort(high)
