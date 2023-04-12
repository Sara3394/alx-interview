#!/usr/bin/python3

"""This is a script which reads stdin line by line and computes metrics"""

import sys


def print_statistics(dicsc, size):
    """ a function that takes two arguments """
    print("File size: {}".format(size))
    for i in sorted(dicsc.keys()):
        if dicsc[i] != 0:
            print("{}: {}".format(i, dicsc[i]))


size = 0
cnt = 0
stas = {"200": 0,
        "301": 0, 
        "400": 0, 
        "401": 0, 
        "403": 0,
        "404": 0, 
        "405": 0, 
        "500": 0}


try:
    for line in sys.stdin:
        if cnt != 0 and cnt % 10 == 0:
            print_statistics(stas, size)

            statlist = line.split()
            cnt += 1

            try:
               size += int(statlist[-1])
            except:
                pass
            
            try:
                if statlist[-2] in stas:
                    stas[statlist[-2]] += 1
            except:
                pass
    print_statistics(stas, size)


except KeyboardInterrupt:
    print_statistics(stas, size)
    raise
