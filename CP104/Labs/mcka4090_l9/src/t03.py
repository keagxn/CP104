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
from functions import parse_code

#--------Constants--------#


#--------Inputs--------#
product_code = input("Enter a product code: ")

#--------Calculations--------#
pc, pi, pq = parse_code(product_code)


#--------Output--------#
print(f"Category:  {pc}")
print(f"ID:        {pi}")
print(f"Qualifier: {pq}")