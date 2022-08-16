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
from functions import list_indexes
from functions import list_positives

#--------Constants--------#


#--------Inputs--------#
values = list_positives()
target = int(input("Enter target: "))

#--------Calculations--------#
indexes = list_indexes(values, target)

#--------Output--------#
print(indexes)