"""
Program: UPC Validator
Author: Claude-henri Gilbert
Purpose: This program checks whether a 12-digit UPC-A
         barcode is valid by calculating its check digit.
Starter Code: No starter code used.
Date: October 29, 2026
"""

def find_UPC(upc):

    odd_sum = 0
    even_sum = 0

    for i in range(0, 11, 2):
        odd_sum += int(upc[i])

    for i in range(1, 11, 2):
        even_sum += int(upc[i])

    total = (odd_sum * 3) + even_sum

    check_digit = (10 - (total % 10)) % 10

    return check_digit