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
from functions import ia_hours

#--------Constants--------#


#--------Inputs--------#
ia_count = int(input("Number of IAs: "))

#--------Calculations--------#
total_hours = ia_hours(ia_count)

#--------Output--------#
print()
print(f"Total marking hours for all IAs: {total_hours:.2f}")