"""
Program: UPC Validator
Author: Claude-henri Gilbert
Purpose: This program checks whether a 12-digit UPC-A
         barcode is valid by calculating its check digit.
Starter Code: No starter code used.
Date: October 29, 2026
"""


def find_UPC(upc):
    """Calculate and return the correct UPC-A check digit."""

    odd_sum = 0
    even_sum = 0

    # Calculate the sum of odd-position digits
    for i in range(0, 11, 2):
        odd_sum += int(upc[i])

    # Calculate the sum of even-position digits
    for i in range(1, 11, 2):
        even_sum += int(upc[i])

    # Multiply odd sum by 3 and add even sum
    total_sum = (odd_sum * 3) + even_sum

    # Calculate the expected check digit
    check_digit = (10 - (total_sum % 10)) % 10

    return check_digit

upc = input("Enter a 12-digit UPC: ")

first_11 = upc[:11]

actual_check_digit = int(upc[11])

print()
print(f"The first 11 digits are '{first_11}'.")
print(f"The provided check digit is '{upc[11]}'.")

print()
print("Calculating...")

expected_check_digit = find_UPC(first_11)
print("Expected check digit:", expected_check_digit)

if actual_check_digit == expected_check_digit:
    print()
    print("This is a VALID UPC.")
else:
    print()
    print("This is an INVALID UPC.")