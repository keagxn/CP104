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
from functions import day_of_week

#--------Constants--------#


#--------Inputs--------#
day_number = int(input("Day of week: "))

#--------Calculations--------#
day = day_of_week(day_number)

#--------Output--------#
print(f'day_of_week({day_number}) > "{day}"')
