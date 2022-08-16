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
from functions import get_addresses

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
fh = open('addresses.txt', 'r', encoding = 'utf-8')

addresses = get_addresses(fh)

fh.close()

for i in addresses:
    print(i)

#--------Output--------#