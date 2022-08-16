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
from random import uniform

#--------Question1--------#
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    if value_type == "float":
        
        for i in range(rows):
            matrix.append([])
            
            for j in range(cols):
                matrix[i].append(uniform(low, high))
                
    else:
        for i in range(rows):
            matrix.append([])
            
            for j in range(cols):
                matrix[i].append(randint(low, high))

    return matrix

#--------Question3--------#
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
    matrix - a 2D list of values (2D list)
    value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
    None.
    -------------------------------------------------------
    """
    print(" ", end="")
    
    for x in range(len(matrix[0])):
        print("{:>7d}".format(x), end="")
        
    print()
    
    if(value_type == "float"):
        
        for x in range(len(matrix)):
            
            print("{:>2.0f}".format(x), end="")
            
            for y in range(len(matrix[x])):
                num = matrix[x][y]
                
                print("{:>7.2f}".format(float(num)), end="")
            print()
    if(value_type == "int"):
        
        for x in range(len(matrix)):
            
            print("{:>2d}".format(x), end="")
            
            for y in range(len(matrix[x])):
                
                print("{:>7d}".format(matrix[x][y]), end="")
                print()
    return

#--------Question6--------#
def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
    Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
    matrix - a 2D list of numbers (2D list of float/int)
    Returns:
    smallest - the smallest number in matrix (float/int)
    largest - the largest number in matrix (float/int)
    total - the total of the numbers in matrix (float/int)
    average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0
    
    for x in range(len(matrix)):
        
        for y in range(len(matrix[x])):
            
            num = matrix[x][y]
            
            if(num < smallest):
                smallest = num
                
            if(num > largest):
                largest = num
                
            total += num
            count += 1
            average = total / count
            
    return smallest, largest, total, average

#--------Question8--------#
def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
    matrix - a 2D list of numbers (2D list)
    n - the target value (float)
    Returns:
    loc - a list of the row and column location of
    the the first value smaller than n in values,
    an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    found = False
    
    for x in range(len(matrix)):
        
        for y in range(len(matrix[x])):
            
            num = matrix[x][y]
            
            if(num < n):
                
                loc.append(x)
                loc.append(y)
                found = True
                break
            
            if(found == True):
                
                break
            
    return loc

#--------Question13--------#
def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
    matrix - the matrix to multiply (2D list of int/float)
    num - the number to multiply by (int/float)
    Returns:
    None
    ------------------------------------------------------
    """
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            num1 = matrix[x][y]
            matrix[x][y] = num1 * num
    return























