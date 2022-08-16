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
from functions import product_largest

#--------Constants--------#


#--------Inputs--------#
v1 = float(input("Input value 1: "))
v2 = float(input("Input value 2: "))
v3 = float(input("Input value 3: "))

#--------Calculations--------#
product = product_largest(v1, v2, v3)

#--------Output--------#
print(f'product_largest({v1:.0f}, {v2:.0f}, {v3:.0f}) > {product:.0f}')