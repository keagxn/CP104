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
from functions import wind_speed

#--------Constants--------#


#--------Inputs--------#
speed = int(input("Wind speed (km/h): "))

#--------Calculations--------#
category = wind_speed(speed)

#--------Output--------#
print(f"Category: {category}")