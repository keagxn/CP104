"""
-------------------------------------------------------
Lab 2, Task 7
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-24"
-------------------------------------------------------
"""

f = int(input("Number of flyers:"))

n = int(input("Number of volunteers:"))

fn = f // n

fl = f % n

print("Flyers per volunteer: ", fn)

print("Flyers left over: ", fl)