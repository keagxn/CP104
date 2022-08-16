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
from functions import mow_lawn 

#--------Constants--------#


#--------Inputs--------#
width = int(input("Width (m): "))

length = int(input("Length (m): "))

speed = int(input("Speed (m^2/minute): "))

#--------Calculations--------#
time = mow_lawn(width, length, speed)

#--------Output--------#
print()
print(f"Mowing the law takes {time:.0f} minutes")