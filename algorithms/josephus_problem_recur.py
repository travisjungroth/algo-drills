"""
ID: 071844a2-e4ec-462d-b994-410c87ab6fca
https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
https://en.wikipedia.org/wiki/Josephus_problem
"""


def josephus_problem_recur(n: int, k: int) -> int:
    """1-indexed, k-skips, Josephus problem, recursively."""
    if n == 1:
        return 1
    return (josephus_problem_recur(n - 1, k) + k - 1) % n + 1
