"""
-------------------------------------------------------
Lab 2, Task 10
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-24"
-------------------------------------------------------
"""

cost = float(input("Food Charge:($):"))

tax = float(input("Sales Tax in (%):"))

tip = float(input("Tip in (%):"))

print("Cost of meal:")

print(f"Subtotal: ${cost:0.2f}")

taxcalc = (cost / 100) * tax

print(f"Tax: ${taxcalc:0.2f}")

tipcalc = (cost / 100) * tip

print(f"Tip: ${tipcalc:0.2f}")

total = cost + tipcalc + taxcalc

print(f"Total: ${total:0.2f}")