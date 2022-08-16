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
from functions import factorial

#--------Constants--------#


#--------Inputs--------#
num = int(input("Number: "))

#--------Calculations--------#
product = factorial(num)

#--------Output--------#
print(f'factorial({num}) -> {product}')