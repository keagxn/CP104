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
from functions import is_hydroxide

#--------Constants--------#


#--------Inputs--------#
chemical = input('Enter a chemical formula: ')

#--------Calculations--------#
hydroxide = is_hydroxide(chemical)

#--------Output--------#
if hydroxide:
    print(f"{chemical} is a hydroxide.")
    
else:
    print(f"{chemical} is not a hydroxide.")