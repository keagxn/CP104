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
from functions import pollution_level

#--------Constants--------#


#--------Inputs--------#
aqi = int(input("Pollution Level: "))

#--------Calculations--------#
level = pollution_level(aqi)

#--------Output--------#
print(f'pollution_level({aqi}) > "{level}"')