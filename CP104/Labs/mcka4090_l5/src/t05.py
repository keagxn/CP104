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
from functions import is_leap

#--------Constants--------#
state = str()

#--------Inputs--------#
year = int(input("Enter a year (>0): "))

#--------Calculations--------#
result = is_leap(year)

if not result == True:
    state = "not "

#--------Output--------#
print(f"{year} is {state}a leap year")