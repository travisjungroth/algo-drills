"""
ID: 0088a99a-fcfb-40de-87ed-d26b98449d3d
"""
from collections import defaultdict
from collections.abc import Callable, Iterable

from hints import T


def counting_sort_dict(items: Iterable[T], key: Callable[[T], int] = lambda x: x) -> Iterable[T]:
    groups = defaultdict(list)
    for item in items:
        groups[key(item)].append(item)
    for k in range(min(groups), max(groups) + 1):
        yield from groups[k]
