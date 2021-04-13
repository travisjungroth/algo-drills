from collections.abc import MutableSequence


def selection_sort_rec(lst: MutableSequence, i: int = 0) -> None:
    if i >= len(lst) - 1:
        return
    min_value, j = min((value, j) for j, value in enumerate(lst[i:], start=i))
    lst[j] = lst[i]
    lst[i] = min_value
    selection_sort_rec(lst, i + 1)
