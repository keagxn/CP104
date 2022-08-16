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
from functions import employee_payroll

#--------Constants--------#


#--------Inputs--------#


#--------Calculations--------#
total, average = employee_payroll()

#--------Output--------#
print()
print(f"Total payment:   ${total:8,.2f}")
print(f"Average payment: ${average:8,.2f}")