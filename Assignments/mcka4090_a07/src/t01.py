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
from functions import list_factors

#--------Constants--------#


#--------Inputs--------#
num = int(input("Number: "))

#--------Calculations--------#
factors = list_factors(num)

#--------Output--------#
print(factors)