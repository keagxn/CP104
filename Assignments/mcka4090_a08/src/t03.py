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
from functions import common_ending

#--------Constants--------#


#--------Inputs--------#
string1 = input("Enter a string: ")
string2 = input("Enter a second string: ")

#--------Calculations--------#
common = common_ending(string1, string2)

#--------Output--------#
print(common)