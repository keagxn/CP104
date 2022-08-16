"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-24"
-------------------------------------------------------
"""

wage = float(input("Hourly rate of pay:"))

hours = float(input("Hours worked in the week:"))

pay = hours * wage

print(f"Total pay for the week: ${pay:0.2f}")
