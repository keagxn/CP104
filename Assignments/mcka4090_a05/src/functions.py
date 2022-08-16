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
def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    
    for i in range(1, num):
        
        product += product * i
        
    return product

#--------Question2--------#
def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every
    five minutes given the number of calories burned per minute
    an the total number of minutes run.
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - calories burned per minute (float)
        minutes - total number of minutes ran (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"calories_burned({per_minute}, {minutes})")
    
    for minute in range(5, minutes + 1, 5):
        
        calories = minute * per_minute
        
        print(f"{minute:3d}:{calories:6.1f}")
        
    return

#--------Question3--------#
def open_triangle(num_rows):
    """
    ------------------------------------------------------
    Takes integer parameter and prints a triangle of # characters with empty center
    Use:
    ------------------------------------------------------
    Parameters:
        num_rows - number of rows in triangle
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(2, num_rows + 2):
        
        print(("#" + (" " * (i - 2) + "#")))
        
    return

#--------Question4--------#
def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"multiplication_table({start}, {stop})")
    
    print("       ", end="")
    
    for num in range(start, stop + 1):
        
        print(f"{num:5d}", end="")

    print()
    
    dashes = "-----" * (stop - start + 1)
    
    print(f"       {dashes}")

    for num1 in range(start, stop + 1):
        
        print(f"{num1:5d} |", end="")

        for num2 in range(start, stop + 1):
            
            product = num1 * num2
            
            print(f"{product:5d}", end="")

        print()

    return

#--------Question5--------#
def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    
    for i in range(start, start + (count * increment), increment):
        
        total += i

    return total


























