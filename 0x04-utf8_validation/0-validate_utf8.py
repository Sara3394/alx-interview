#!/usr/bin/python3
"""
checks and validates UTF-8 encoding
"""


def validUTF8(data):

    no_of_bytes = 0
    for numbers in data:
        number_of_bin = format(numbers, '#010b')[-8:]
        if no_of_bytes == 0:

            for bit in number_of_bin:
                if bit == '0':
                    break
                no_of_bytes += 1

            if no_of_bytes == 0:
                continue

            if no_of_bytes == 1 or no_of_bytes > 4:
                return False
        else:

            if not number_of_bin.startswith('10'):
                return False

        no_of_bytes -= 1

    return no_of_bytes == 0
