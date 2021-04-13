from collections.abc import Iterable, Sequence


def dfs_components_grid(grid: Sequence[Sequence[int]]) -> Iterable[set[tuple[int, int]]]:
    unvisited = {(r, c) for r, row in enumerate(grid) for c, n in enumerate(row) if n}
    while unvisited:
        start = unvisited.pop()
        component = {start}
        stack = [start]
        while stack:
            r, c = stack.pop()
            adjacent = {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)}
            visit = unvisited & adjacent
            unvisited -= visit
            component |= visit
            stack.extend(visit)
        yield component
