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
from functions import gic

#--------Constants--------#


#--------Inputs--------#
value = int(input("Enter the GIC purchase value: $"))
years = int(input("Enter the number of years invested: "))
rate = float(input("Enter the GIC interest rate (%): "))

#--------Calculations--------#
final_value = gic(value, years, rate)

#--------Output--------#