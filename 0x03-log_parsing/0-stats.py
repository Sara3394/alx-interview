#!/usr/bin/python3

"""This is a script which reads stdin line by line and computes metrics"""

import sys


def prinstats(dicst, file_size):
    """ reads from stdin & prints status """
    print("File size: {:d}".format(file_size))
    for i in sorted(dicst.keys()):
        if dicst[i] != 0:
            print("{}: {:d}".format(i, dicst[i]))


stats = {"200": 0, 
         "301": 0, 
         "400": 0,
         "401": 0, 
         "403": 0,
         "404": 0, 
         "405": 0, 
         "500": 0}

cnt = 0
file_size = 0

try:
    for line in sys.stdin:
        if cnt != 0 and cnt % 10 == 0:
            prinstats(stats, file_size)

        statlist = line.split()
        cnt += 1

        try:
            file_size += int(statlist[-1])
        except:
            pass

        try:
            if statlist[-2] in stats:
                stats[statlist[-2]] += 1
        except:
            pass
    prinstats(stats, file_size)


except KeyboardInterrupt:
    prinstats(stats, file_size)
    raise
