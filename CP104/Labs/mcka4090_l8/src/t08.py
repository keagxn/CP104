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
from functions import linear_search

#--------Constants--------#


#--------Inputs--------#
a = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]

print(f"Values: {a}")
print()

v = int(input("Chosen Value: "))

#--------Calculations--------#
index = linear_search(a, v)

#--------Output--------#
print(f"Index of {v}: {index}")