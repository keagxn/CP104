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
from functions import feet_to_acres

#--------Constants--------#


#--------Inputs--------#
square_footage = int(input("Square footage: "))

#--------Calculations--------#
acres = feet_to_acres(square_footage)

#--------Output--------#
print()
print(f"{acres:0.2f} acres is equivalent to {square_footage:,.2f} square feet")