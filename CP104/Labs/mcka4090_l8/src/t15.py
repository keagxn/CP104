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
from functions import symmetric_difference

#--------Constants--------#


#--------Inputs--------#
source1 = [10, 3, 10, 3, 1]
source2 = [8, 2, 7, 3, 6, 10, 32, 99]

print(f"Values 1: {source1}")
print(f"Values 2: {source2}")

#--------Calculations--------#
target = symmetric_difference(source1, source2)

#--------Output--------#
print()
print(f"Difference: {target}")