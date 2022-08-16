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
from functions import is_sorted
from functions import list_positives

#--------Constants--------#


#--------Inputs--------#
values = list_positives()

#--------Calculations--------#
in_order, index = is_sorted(values)

#--------Output--------#
print(f"{in_order}, {index}")