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
from functions import interest_table

#--------Constants--------#


#--------Inputs--------#
principal = float(input("Principal: $"))
rate = float(input("Interest rate (%): "))
payment = float(input("Monthly payment: $"))

#--------Calculations--------#
interest_table(principal, rate, payment)

#--------Output--------#
print(f"""interest_table({principal}, {rate}, {payment}) >""")