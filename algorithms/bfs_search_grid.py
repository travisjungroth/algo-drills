"""
b2d4ac17-3a7f-478f-8949-da86687be458
"""
from collections import deque
from collections.abc import Sequence


def bfs_search_grid(grid: Sequence[Sequence[int]], start: tuple[int, int], goal: tuple[int, int]) -> bool:
    rows = range(len(grid))
    cols = range(len(grid[0]))
    seen = {start}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            return True
        adjacent = {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)}
        for next_node in adjacent - seen:
            seen.add(next_node)
            r1, c1 = next_node
            if r1 in rows and c1 in cols and grid[r1][c1]:
                queue.append(next_node)
    return False
