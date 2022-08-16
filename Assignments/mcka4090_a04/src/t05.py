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
from functions import yee_ha

#--------Constants--------#


#--------Inputs--------#
number = float(input("Integer: "))

#--------Calculations--------#
feedback = yee_ha(number)

#--------Output--------#
print(f'yee_ha({number:.0f}) > "{feedback}"')