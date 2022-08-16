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
from functions import text_analyze

#--------Constants--------#


#--------Inputs--------#
txt = input("Enter a string: ")

#--------Calculations--------#
uppr, lowr, dgts, whtspc = text_analyze(txt)

#--------Output--------#
print(f"upper case letters: {uppr}")
print(f"lower case letters: {lowr}")
print(f"digits: {dgts}")
print(f"whitespace characters: {whtspc}")