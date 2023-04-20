#!/usr/bin/python3
"""
Checks and validates UTF-8 encoding

"""

def decimalToBinary(no):
    #converting decimal to binary
    return bin(no).replace("0b", "")


def validUTF8(data):

    no_of_bytes = 0 
    
    for no in data:
        # the least significant bits of the last block
        bits_per_byte = decimalToBinary(no)
        if no_of_bytes == 0:

            for bit in bits_per_byte:
                if bit == '0':
                    break
                no_of_bytes += 1

            if no_of_bytes == 0:
                continue

            if no_of_bytes == 1 or no_of_bytes > 4:
                return False
        else:

            if not bit_per_byte.startswith('10'):
                return False

        no_of_bytes -= 1

    return no_of_bytes == 0
