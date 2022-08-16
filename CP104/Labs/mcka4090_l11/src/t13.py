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
from functions import print_matrix_num, generate_matrix_num, scalar_multiply
from random import randint

rows = randint(1, 9)
cols = randint(1, 9)
low = -10
high = 10
value_type = "int"

print("Matrix before scalar multiplication: ")
matrix = generate_matrix_num(rows, cols, low, high, value_type)
print_matrix_num(matrix, value_type)
print()
num = int(input("Enter number: "))
print()
print("Matrix after scalar muliplication: ")
scalar_multiply(matrix, num)
print_matrix_num(matrix, value_type)