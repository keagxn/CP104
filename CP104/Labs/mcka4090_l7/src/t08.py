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
from functions import budget

#--------Constants--------#


#--------Inputs--------#
available = int(input("Monthly budget: $"))

#--------Calculations--------#
expenses, balance, status = budget(available)

#--------Output--------#
print(f"total Expenses: ${expenses:.2f}")
print(f"{status}: ${balance:.2f}")