#!/usr/bin/python3

"""

given a pile of coins of different values
this script finds the minimum number of coins
needed to meet a given amount total.
"""

def makeChange(coins, total):
    """ Returns: fewest number of coins needed """
    
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1
    coins_needed = 0
    coins.sort()
    coins.reverse()   
    for coin in coins:
        while coin <= total:
            total -= coin
            coins_needed += 1
        if (total == 0):
            return coins_needed
    return -1

