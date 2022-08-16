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
from functions import multiply_fractions

#--------Constants--------#


#--------Inputs--------#
num1 = int(input("Numerator 1: "))

denom1 = int(input("Denominator 1: "))

num2 = int(input("Numerator 2: "))

denom2 = int(input("Denominator 2: "))

#--------Calculations--------#
numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)

#--------Output--------#
print()
print(f"Result: {numerator}/{denominator} = {product}")