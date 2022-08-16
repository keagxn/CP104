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
from functions import is_valid_isbn

#--------Constants--------#


#--------Inputs--------#
isbn = input("Enter isbn: ")

#--------Calculations--------#
valid = is_valid_isbn(isbn)

#--------Output--------#
print(valid)