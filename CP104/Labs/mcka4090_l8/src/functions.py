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

from random import randint

#--------Question4--------#
def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    
    for _ in range(n):
        
        num = randint(low,high)
        values.append(num)
        
    return values

#--------Question7--------#
def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    values.sort()
    positives = 0
    negatives = 0
    evens = 0
    odds = 0
    zeros = 0
    
    for num in values:
        
        if num > 0:
            positives = positives + 1
            
            if num % 2 == 0:
                
                evens = evens + 1
                
            else:
                
                odds = odds + 1
                
        elif num == 0:
            
            zeros = zeros + 1
            evens = evens + 1
            
        else:
            
            negatives = negatives + 1
            
            if num % 2 == 0:
                
                evens = evens + 1
                
            else:
                
                odds = odds + 1
                
    return negatives, positives, zeros, evens, odds

#--------Question8--------#
def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    Use: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = 0
    
    while index < len(a) and a[index] != v:
        
        index = index + 1
        
    if index == len(a):
        
        index = -1
        
    return index
    
#--------Question13--------#
def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    
    for i in source1:
        
        if i not in target:
            
            target.append(i)
            
    for i in source2:
        
        if i not in source1 and i not in target:
            
            target.append(i)
            
    return target

#--------Question15--------#
def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        
        if i not in source2 and i not in target:
            
            target.append(i)
            
    for i in source2:
        
        if i not in source1 and i not in target:
            
            target.append(i)
            
    return target













