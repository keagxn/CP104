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
from functions import date_extract

#--------Constants--------#


#--------Inputs--------#
date = int(input("Enter a date in the format MMDDYYYY: "))

#--------Calculations--------#
year, month, day = date_extract(date)

#--------Output--------#
print()
print(f"The reformatted date: {year:04d}/{month:02d}/{day:02d}")