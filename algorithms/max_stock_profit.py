"""
ID: cecca0e0-708f-47db-a747-515d90d06470
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def max_stock_profit(prices: list[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a
    different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    current_profit = 0
    current_min_price = None
    for price in prices:
        if current_min_price is None or price < current_min_price:
            current_min_price = price
        elif price - current_min_price > current_profit:
            current_profit = price - current_min_price
    return current_profit
