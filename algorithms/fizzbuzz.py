"""
ID: 5dff0fc6-c3b5-4735-b353-1962835eeed1
https://leetcode.com/problems/fizz-buzz/
"""


def fizzbuzz(n: int) -> list[str]:
    """Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i if non of the above conditions are true."""
    for i in range(1, n + 1):
        if not i % 15:
            yield "FizzBuzz"
        elif not i % 3:
            yield "Fizz"
        elif not i % 5:
            yield "Buzz"
        else:
            yield str(i)
