#!/usr/bin/python3
"""0-lockboxes.py - Lockboxes"""


def canUnlockAll(boxes):
    """ceate a set to keep track of the boxes we've opened"""
    unlocked = {0}
    
  
    keys = set(boxes[0])

    while keys:
        box = keys.pop()
        unlocked.add(box)
        keys.update(boxes[box])

    return len(unlocked) == len(boxes)
