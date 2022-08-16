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
from functions import power_of_two

#--------Constants--------#


#--------Inputs--------#
target = int(input("Enter the target: "))

#--------Calculations--------#
power = power_of_two(target)

#--------Output--------#
print(f"power_of_two({target}) > {power}")