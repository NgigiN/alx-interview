#!/usr/bin/python3
"""
determines the number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    returns the fewest number of coins neede to meet a given amount

    Args:
            coins: list of the values of the coins in your possession
            total: the amount to be met
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_counter = 0

    for coin in coins:
        while total >= coin:
            total = total - coin
            coin_counter = coin_counter + 1

    if total == 0:
        return coin_counter
    else:
        return -1
