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
from functions import find_longest

#--------Constants--------#
fh = open("words.txt", "r")

#--------Inputs--------#


#--------Calculations--------#
word = find_longest(fh)
fh.close()

#--------Output--------#
print("file 'words.txt' open for reading")
print(f"'{word}' is the last longest word")