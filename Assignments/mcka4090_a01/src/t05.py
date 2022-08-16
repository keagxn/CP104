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
prin = float(input("Principal($): "))

interest = float(input("Interest (decimal): "))

years = int(input("Number of years: "))

tpy = int(input("Number of times interest compounded per year: "))

total = prin * ((1 + (interest / tpy)) ** (years * tpy))

print(f"Balance: ${total:0.2f}")