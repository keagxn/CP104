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
from functions import range_total

#--------Constants--------#


#--------Inputs--------#
start = int(input("Start: "))
increment = int(input("Increment: "))
count = int(input("Count: "))

#--------Calculations--------#
total = range_total(start, increment, count)

#--------Output--------#
print(f"The total is {total}.")