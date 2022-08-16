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
from functions import stats

#--------Constants--------#


#--------Inputs--------#
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))

#--------Calculations--------#
smallest, largest, total, average = stats(matrix)

#--------Output--------#