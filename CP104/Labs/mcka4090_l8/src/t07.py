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
from functions import list_categorize
from random import randint

#--------Constants--------#


#--------Inputs--------#
values = [randint(-100, 100) for i in range(10)]

print(f"Values: {values}")
print()

#--------Calculations--------#
negatives, positives, zeroes, evens, odds = list_categorize(values)

#--------Output--------#
print(f"Negatives: {negatives}")
print(f"Positives: {positives}")
print(f"Zeroes: {zeroes}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")