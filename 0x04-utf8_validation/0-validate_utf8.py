#!/usr/bin/python3
"""
checks and validates UTF-8 encoding
"""


def validUTF8(data):

    no_of_bytes = 0
    for no in data:
        bits_per_byte_block = replace("0b", "")
        if no_of_bytes == 0:

            for bit in bits_per_byte_block:
                if bit == '0':
                    break
                no_of_bytes += 1

            if no_of_bytes == 0:
                continue

            if no_of_bytes == 1 or no_of_bytes > 4:
                return False
        else:

            if not bits_per_byte_block.startswith('10'):
                return False

        no_of_bytes -= 1

    return no_of_bytes == 0
