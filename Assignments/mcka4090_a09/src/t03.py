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
from functions import file_stats

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
fh = open('addresses.txt')
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

#--------Output--------#
print(f"# of upper case: {ucount}")
print(f"# of lower case: {lcount}")
print(f"# of digits: {dcount}")
print(f"# of whitespace: {wcount}")