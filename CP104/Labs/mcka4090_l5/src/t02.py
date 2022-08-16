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
from functions import get_weight

#--------Constants--------#


#--------Inputs--------#
mass = float(input("Enter mass (kg): "))

#--------Calculations--------#
weight, message = get_weight(mass)

#--------Output--------#
print()
print(f"Weight: {weight:.1f} N")
print(f"Object is: {message}")