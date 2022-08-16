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
from functions import customer_first

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#


#--------Output--------#
print('Find customer with earliest sign-in')

fh = open('customers.txt')
customer = customer_first(fh)
fh.close()

print(f"{customer}")