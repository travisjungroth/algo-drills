"""
ID: 51ad98ff-3279-4914-9d04-28dbe80b23ea
https://leetcode.com/problems/fibonacci-number/
"""
from functools import cache


@cache
def fibonacci(n: int) -> int:
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence,
    called the Fibonacci sequence, such that each number is the sum
    of the two preceding ones, starting from 0 and 1.
    That is, F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
