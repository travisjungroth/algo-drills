"""
ID: a34d91af-d8d8-4b4e-bde6-d2443174a222
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""


def josephus_problem_iter(n: int, k: int) -> int:
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1
