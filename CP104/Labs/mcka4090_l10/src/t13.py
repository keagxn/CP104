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
from functions import file_copy

#--------Constants--------#
fh_1 = open("words.txt", "r")
fh_2 = open("new_words.txt", "w")

#--------Inputs--------#


#--------Calculations--------#
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()

#--------Output--------#
print("Copying 'words.txt' to 'new_words.txt'")