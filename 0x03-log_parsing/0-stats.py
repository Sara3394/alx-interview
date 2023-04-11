#!/usr/bin/python3

"""This is a script which reads stdin line by line and computes metrics"""

import sys


def print_statistics(dic_status_codes, size):
    """ a function that takes two arguments
        dic_status_codes - status codes dict
        size - total size of the file
    """
    print("File size: {}".format(size))
    for i in sorted(dic_status_codes.keys()):
        if dic_status_codes[i] != 0:
            print("{}: {}".format(i, dic_status_codes[i]))


size = 0
cnt = 0
dic_status_codes = {"200": 0,
                    "301": 0, 
                    "400": 0, 
                    "401": 0, 
                    "403": 0,
                    "404": 0, 
                    "405": 0, 
                    "500": 0}


try:
    for line in sys.stdin:
        if cnt != 0 and count % 10 == 0:
            print_statistics(dic_status_codes, size)

            statlist = line.split()
            cnt += 1

            try:
               size += int(statlist[-1])
            except:
                pass
            try:
                if statlist[-2] in dic_status_codes:
                    dic_status_codes[statlist[-2]] += 1
            except:
                pass
    print_statistics(dic_status_codes, size)


except KeyboardInterrupt:
    print_statistics(dic_status_codes, size)
    raise
