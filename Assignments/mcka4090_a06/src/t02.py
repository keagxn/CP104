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
from functions import is_prime

#--------Constants--------#


#--------Inputs--------#
num = int(input("Enter a number: "))

#--------Calculations--------#
prime = is_prime(num)

#--------Output--------#
print()
print(f"is_prime({num:d}) > {prime}")