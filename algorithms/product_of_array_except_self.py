"""
ID: b824470f-c5b9-4f95-8c56-32baeaaacfc0
https://leetcode.com/problems/product-of-array-except-self/
"""
from itertools import accumulate
from operator import mul


def product_of_array_except_self(nums: list[int]):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal
    to the product of all the elements of nums except nums[i].
    """
    lefts = accumulate(nums, func=mul, initial=1)
    rights = list(accumulate(nums[::-1], func=mul, initial=1))[-2::-1]
    return map(mul, lefts, rights)
