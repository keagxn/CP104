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
from functions import digit_count

#--------Constants--------#


#--------Inputs--------#
num = int(input("Enter an integer: "))

#--------Calculations--------#
count = digit_count(num)

#--------Output--------#
print()
print(f"digit_count({num}) > {count}")