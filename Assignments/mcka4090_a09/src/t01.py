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
from functions import file_head

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
linecount = int(input("Number of lines to print: "))
fh = open('t01.txt')
file_head(fh, linecount)
fh.close()

#--------Output--------#