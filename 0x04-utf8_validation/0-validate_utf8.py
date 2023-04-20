#!/usr/bin/python3
"""
checks and validates UTF-8 encoding
"""


def validUTF8(data):

    number_of_bytes = 0
    for numbers in data:
        # prints the 8least sig bits
        number_of_bin = format(numbers, '#010b')[-8:]
        if number_of_bytes == 0:

            for bit in number_of_bin:
                if bit == '0':
                    break
                number_of_bytes += 1

            if number_of_bytes == 0:  # 1 byte characters
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:

            # Bytes which are a part of
            # a UTF-8 character must adhere
            # to the pattern `10xxxxxx`.
            if not number_of_bin.startswith('10'):
                return False

        # We reduce the number of bytes
        # to process by 1 after each integer.
        number_of_bytes -= 1

    return number_of_bytes == 0
