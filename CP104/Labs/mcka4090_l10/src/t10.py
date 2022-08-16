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
from functions import count_frequency_word

#--------Constants--------#
fh = open("words.txt", "r")
print("file 'words.txt' open for reading")
word = input("Word to count: ")

#--------Inputs--------#


#--------Calculations--------#
count = count_frequency_word(fh, word)
fh.close()

#--------Output--------#
print(f"'{word}' appears {count} time(s)")