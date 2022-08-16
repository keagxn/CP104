"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-17"
-------------------------------------------------------
"""

sales = int(input("Enter the total sales: $"))

TAX = 22.50

total = sales / 100 * TAX

print('')

print("Projected Tax Report")

print("--------------------------")

print(f"Total sales:   $ {sales:<0.2f}")

print(f"Annual tax:    % {TAX:<0.2f}")

print("--------------------------")

print(f"Tax:           $  {total:<0.2f}")