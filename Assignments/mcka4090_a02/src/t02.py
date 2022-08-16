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

num = int(input("Enter a positive digit number: "))

base = 10

fg = num // base
sg = num % base

#convert individual into string my calling psoition 0 and pos 1

answer = fg - sg

print(f"The difference of the digits of {num} is {answer}")