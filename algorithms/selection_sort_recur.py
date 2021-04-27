"""
ID: 66b1e371-f33a-4afb-9dbb-f85d35204c10
Python Algorithms, Page 75
"""
from collections.abc import MutableSequence

from hints import T


def selection_sort_recur(seq: MutableSequence[T], i=0) -> None:
    """Use selection sort recursively on a list in-place."""
    if i >= len(seq) - 1:
        return
    min_val = min(seq[i:])
    min_val_i = seq.index(min_val, i)
    seq[min_val_i] = seq[i]
    seq[i] = min_val
    selection_sort_recur(seq, i + 1)
