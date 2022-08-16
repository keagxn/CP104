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
from functions import vowel_count

#--------Constants--------#


#--------Inputs--------#
s = input("Enter a string: ")

#--------Calculations--------#
count = vowel_count(s)

#--------Output--------#
print(f"There are {count} vowels.")