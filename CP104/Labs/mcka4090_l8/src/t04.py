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
from functions import generate_integer_list

#--------Constants--------#


#--------Inputs--------#
n=int(input("Number of values: "))
low = int(input("Low Value: "))
high = int(input("High value: "))

#--------Calculations--------#
values = generate_integer_list(n, low, high)

#--------Output--------#
print()
print(f"Values: {values}")