#!/usr/bin/python3
"""
Prime Game
"""


def primesList(n):
    """Return prime numbers list
    """
    primeNumbers = []
    filters = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filters[prime]):
            primeNumbers.append(prime)
            for i in range(prime, n + 1, prime):
                filters[i] = False
    return primeNumbers


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        primeNumbers = primesList(nums[i])
        if len(primeNumbers) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben < Maria:
        return 'Maria'
    elif Maria < Ben:
        return 'Ben'
    return None
