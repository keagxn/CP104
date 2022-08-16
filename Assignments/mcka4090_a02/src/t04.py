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
balloon = int(input("Number of balloons: "))

child = int(input("Number of children: "))

ans = int(balloon) // int(child)

remainder = int(balloon) % int(child)

print("")

print(f"Each child receives {ans} balloons")

print(f"Balloons that won't be distributed: {remainder}")