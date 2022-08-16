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
from functions import rgb_mix

#--------Constants--------#


#--------Inputs--------#
rgb1 = input("RGB1: ")
rgb2 = input("RGB2: ")

#--------Calculations--------#
colour = rgb_mix(rgb1, rgb2)

#--------Output--------#
print(f'rgb_mix("{rgb1}", "{rgb2}") > "{colour}"')