#!/usr/bin/python3
"""0-lockboxes.py - Lockboxes"""


def canUnlockAll(boxes):
    """canUnlockAll - determines if all the boxes can be opened"""
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)
