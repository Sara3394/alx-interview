#!/usr/bin/python3
"""
Given a pile of coins of different values,
this script finds the minimum number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ Returns: fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1
    
    coinsNeeded = 0
    coins.sort()
    coins.reverse()
    
    for coin in coins:
        while coin <= total:
            total -= coin
            coinsNeeded += 1
        if (total == 0):
            return coinsNeeded
    return -1
