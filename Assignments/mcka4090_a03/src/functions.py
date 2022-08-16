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

#CHECK BACK
#1 CONSTANT
#5 N/A ... Provide the function docstring (documentation) following the CP104 style. Align the results as shown sample execution using formatted printing

RATE = 43560
from random import randint

#--------Question1--------#
def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    convert = square_footage / RATE
    return convert

#--------Question2--------#
def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    time = (width * length) / (speed)
    return time

#--------Question3--------#

def date_extract(date):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    month = date // 1000000
    day = date // 10000 % 100
    year = date % 10000
    return year, month, day

#--------Question4--------#
def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = numerator / denominator
    return numerator, denominator, product

#--------Question5--------#
def math_quiz():
    """
    -------------------------------------------------------
    Displays two random numbers between 0 and 999 that are to be added, 
    asks a user to enter an answer, then displays the user answer along with the expected answer
    Use: None
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    ------------------------------------------------------
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    ans = num1 + num2
    
    print(f"{num1:>5d}")
    print(f"+ {num2:>3d}")
    print()
    
    user = int(input("Your answer: "))
    
    print()    
    print(f"Your answer: {user:>4d}")
    print(f"Expected: {ans:>7d}")
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















