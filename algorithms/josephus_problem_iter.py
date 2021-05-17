"""
ID: 071844a2-e4ec-462d-b994-410c87ab6fca
https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
"""


def josephus_problem_iter(n: int, k: int) -> int:
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1


