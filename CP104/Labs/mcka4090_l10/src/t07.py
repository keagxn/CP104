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
from functions import append_max_num

#--------Constants--------#
fh = open("numbers.txt", "r+")

#--------Inputs--------#


#--------Calculations--------#
num = append_max_num(fh)
fh.close()

#--------Output--------#
print("file 'numbers.txt' open for reading and writing")
print(f"{num} is appended")