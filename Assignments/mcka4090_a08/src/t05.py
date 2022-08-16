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
from functions import is_word_chain

#--------Constants--------#


#--------Inputs--------#
word_list = input("Enter a list of strings separated by space: ").split(" ")

#--------Calculations--------#
word_chain = is_word_chain(word_list)

#--------Output--------#
print(word_chain)