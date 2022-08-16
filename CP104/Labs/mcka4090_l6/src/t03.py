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
from functions import sum_all

#--------Constants--------#


#--------Inputs--------#
start = int(input("Enter the start: "))
finish = int(input("Enter the end: "))
increment = int(input("Enter the increment: "))

#--------Calculations--------#
total = sum_all(start, finish, increment)

#--------Output--------#
print(f"The sum of all numbers from 5 to 10 increment 1 is: {total}")