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

#--------Question1--------#
def list_factors(num):
    """
    -------------------------------------------------------
    creates a list of factors of num
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        factors - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    i = 0
    factors = []
    
    while i <= num / 2:
        
        i += 1
        
        if num % i == 0:
            
            factors.append(i)
            
    return factors

#--------Question2--------#
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    value = int(input("Enter a positive number: "))
    
    while value != 0:
        
        if value > 0:
            
            numbers.append(value)
            
        value = int(input("Enter a positive number: "))
        
    return numbers

#--------Question3--------#
def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list)
        target - value to look for in num_list (*)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    
    for i in range(len(values)):
        
        if values[i] == target:
            
            locations.append(i)
            
    return locations

#--------Question4--------#
def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(subtrahend)):
        
        indexes = list_indexes(minuend, subtrahend[i])
        
        for j in range(len(indexes) - 1, -1, -1):
            
            minuend.pop(indexes[j])
    return

#--------Question5--------#
def is_sorted(values):
    """
    -------------------------------------------------------
    Returns the sum of the even numbers in values.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    i = 0
    
    while in_order and i < len(values) - 1:
        
        i += 1
        
        if (values[i] < values[i - 1]):
            
            in_order = False
            index = i
            
    return in_order, index























