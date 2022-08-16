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
from functions import file_integers

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
fh = open('numbers.txt')
numbers = file_integers(fh)
fh.close()

print(f"{numbers}")

#--------Output--------#