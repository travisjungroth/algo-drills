"""
ID: f6c05456-776c-4664-8470-ed3c2ff29a94
https://leetcode.com/problems/climbing-stairs/
"""
from functools import cache


@cache
def climbing_stairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    if n < 3:
        return n
    return climbing_stairs(n - 1) + climbing_stairs(n - 2)
