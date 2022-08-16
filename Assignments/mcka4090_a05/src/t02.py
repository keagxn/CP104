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
from functions import calories_burned

#--------Constants--------#


#--------Inputs--------#
per_minute = float(input("Calories per Min: "))
minutes = int(input("Minutes: "))

#--------Calculations--------#
calories_burned(per_minute, minutes)

#--------Output--------#