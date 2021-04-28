"""
ID: a01ea147-459f-43c0-8f14-ec50aedd1fa9
https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
Grokking Algorithms, Page 161
Python Algorithms, Page 143
There are many versions of the knapsack problem. This is one of the simplest that still benefits from
 some form of dynamic programming.
Iterative dynamic programming usually means making a matrix of previous calculations and sub-calculations.
If you only need to access the very last round of calculations (like this problem) you can just use a list.
"""
from typing import Sequence


def knapsack_simple(weights: Sequence[int], values: Sequence[int], capacity: int):
    """0-1 knapsack problem. Just return the max value."""
    # Each index is a sub-capacity and each value the best value for that sub-capacity so far.
    best_values = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        # Iterate backwards so we don't take things twice. Forwards would be the unbounded version of the problem.
        for sub_capacity in range(capacity, 0, -1):
            if weight <= sub_capacity:
                new_value = best_values[sub_capacity - weight] + value
                best_values[sub_capacity] = max(best_values[sub_capacity], new_value)
    return best_values[-1]
