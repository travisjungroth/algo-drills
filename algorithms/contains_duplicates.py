"""
ID: 2f98876c-d458-4fbb-b1b0-28ebe665a6cf
https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicates(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    return not len(set(nums)) == len(nums)
