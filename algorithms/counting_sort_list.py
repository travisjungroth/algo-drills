"""
ID: 29227b58-d1f9-4575-bdf7-13dea23d77fb
https://en.wikipedia.org/wiki/Counting_sort
"""
from collections.abc import Callable, Sequence
from itertools import accumulate

from hints import T


def counting_sort_list(items: Sequence[T], key: Callable[[T], int] = lambda x: x):
    max_value = max(map(key, items))
    count = [0] * (max_value + 1)
    for item in items:
        count[key(item)] += 1
    count = list(accumulate(count, initial=0))
    ret = [None] * len(items)
    for item in items:
        i = count[key(item)]
        ret[i] = item
        count[key(item)] = i + 1
    return ret
