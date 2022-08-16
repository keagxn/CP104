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
from functions import positive_statistics

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
minimum, maximum, total, average = positive_statistics()

#--------Output--------#
print()
print(f"minimum: {minimum:.2f}")
print(f"maximum: {maximum:.2f}")
print(f"total: {total:.2f}")
print(f"average: {average:.2f}")