"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-24"
-------------------------------------------------------
"""

mortgage = float(input("Mortgage principal($):"))

years = int(input("Number of years:"))

months = years * 12

interest = float(input("Yearly interest rate (%):"))

rate = interest / 100.0 / 12.0

top = rate * (1 + rate)**months

bottom = ((1 + rate)**months) - 1

pay = mortgage * (top / bottom)

print(f"The monthly payments are: ${pay:0.2f}")