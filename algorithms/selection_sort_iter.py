"""
ID: 556c4a0f-f488-4a6b-99b4-4d09e006be23
Grokking Algorithms, Page 32
Python Algorithms, Page 75

This implementation is different than the ones in the referenced books, which are different from each other.
It uses methods and functions that do iteration versus for-loops. Just remember it's still O(n^2).
"""
from collections.abc import MutableSequence

from typehints import T


def selection_sort_iter(seq: MutableSequence[T]) -> None:
    """Use selection sort iteratively on a list in-place."""
    for i, _ in enumerate(seq):  # Maybe more Pythonic than range(len(seq))
        min_val = min(seq[i:])
        min_val_i = seq.index(min_val, i)  # First index of min_val at or after i
        seq[min_val_i] = seq[i]
        seq[i] = min_val
