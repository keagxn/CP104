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
from functions import str_distance

#--------Constants--------#


#--------Inputs--------#
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

#--------Calculations--------#
d = str_distance(s1, s2)

#--------Output--------#
print(f"Distance: {d}")