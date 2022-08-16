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
from functions import generate_matrix_num, print_matrix_num

#--------Constants--------#


#--------Inputs--------#
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))
value_type = input("Type of values: ")


#--------Calculations--------#
matrix = generate_matrix_num(rows, cols, low, high, value_type)
print_matrix_num(matrix,type)

#--------Output--------#
