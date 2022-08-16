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

WEEKS = 6

#--------Question3--------#

def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    
    total = 0
    
    for i in range(start, finish + 1, increment):
        
        total += i
    
    return total

#--------Question6--------#

def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    spaces = 0
 
    for i in range(1, height + 1):
 
        for _ in range(1, (height - i) + 1):
            print(end=" ")
     
        while spaces != (2 * i - 1):
            print(char, end="")
            spaces += 1
    
        spaces = 0
        print()
        
    return
    
#--------Question7--------#

def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(0, width + 1):
    
        print(char * i)
    

    for i in range(width, 0, -1):  
          
        for _ in range(0, i - 1):  
            
            print(char, end="")  
            
        print()  

#--------Question12--------#

def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    
    print("Year       Value $")
    print("------------------")
    
    for i in range(0, years + 1, 1):
        
        if i > 0:
        
            value = ((value / 100) * rate) + value
        
        final_value = value
    
        print(f"{i:2d}{final_value:16,.2f}")
    
    return final_value
    
#--------Question14--------#

def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """ 
    
    total_hours = 0
    
    for i in range(1, WEEKS + 1, 1):
        
        print()
        print(f"Week {i}")
        
        for i in range(1, ia_count + 1, 1):
            
            hour = float(input(f"  Marking hours for IA {i}: "))
            
            total_hours = total_hours + hour
        
        
        
    return total_hours
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    