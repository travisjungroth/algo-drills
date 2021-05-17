"""
ID: 9238d625-5cb9-472f-bd90-c9f377402745
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    """
    pairs = {}
    for i, num in enumerate(nums):
        if target - num in pairs:
            return pairs[target - num], i
        pairs[num] = i
