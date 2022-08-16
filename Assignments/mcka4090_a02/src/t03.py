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
date = int(input("Enter a date in the format MMDDYYYY: "))

year = date % 10000

month = date // 1000000

day = (date % 1000000) / 10000

print(f"The reformatted date: {year}/{month}/{day:0.0f}")