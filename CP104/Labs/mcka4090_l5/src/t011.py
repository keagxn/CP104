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
from functions import quadrant

#--------Constants--------#


#--------Inputs--------#
x = float(input("Enter the x coordinate: "))

y = float(input("Enter the y coordinate: "))

#--------Calculations--------#
location = quadrant(x, y)

#--------Output--------#
print()
print(f"Category: {location}")