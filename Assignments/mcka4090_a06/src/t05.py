"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2021-09-17"
-------------------------------------------------------
"""

#--------Imports--------#
from functions import sum_factors

#--------Constants--------#


#--------Inputs--------#
num = int(input("Enter a positive integer: "))

#--------Calculations--------#
total = sum_factors(num)

#--------Output--------#
print()
print(f"sum_factors({num}) > {total}")