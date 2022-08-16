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

GRAVITY = 9.8

INFANT = 2

SENIOR = 65

STUDENT1 = 10

STUDENT2 = 17

ADULT1 = 18

ADULT2 = 64

KID1 = 3

KID2 = 9

#--------Question2--------#
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass * GRAVITY
    message = "empty"
    
    if weight > 1000:
        message = "heavy"
        
    elif weight < 10:
        message = "light"
        
    else:
        message = "average"
        
    return weight, message

#--------Question5--------#
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if year % 4 == 0:
        result = True
        
        if year % 100 == 0:
            result = False
            
            if year % 400 == 0:
                result = True
        
    else:
        result = False
    
    return result

#--------Question9--------#
def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed < 0:
        category = "Unknown"
    
    elif speed > -1 and speed < 39:
        category = "Breeze"
    
    elif speed > 38 and speed < 62:
            category = "Strong Wind"
        
    elif speed > 61 and speed < 89:
                category = "Gale Winds"
                
    elif speed > 88 and speed < 118:
                    category = "Whole Gale"
                
    elif speed > 117:
                        category = "Hurricane"
        
    return category

#--------Question11--------#
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - name of: quadrant, axis, or origin of coordinate x, y (str)
    -------------------------------------------------------
    """
    
    if x > 0 and y > 0:
        location = "Quadrant 1"
        
    elif x < 0 and y > 0:
        location = "Quadrant 2"
        
    elif x < 0 and y < 0:
        location = "Quadrant 3"
        
    elif x > 0 and y < 0:
        location = "Quadrant 4"
    
    elif x == 0 and (y < 0 or y > 0):
        location = "Y-Axis"
        
    elif y == 0 and (x < 0 or x > 0):
        location = "X-Axis"
        
    else:
        location = "Origin"
        
    return location

#--------Question14--------#
def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    
    age = int(input("How old are you? "))
    
    if age <= INFANT:
        price = 0
        
    elif age >= SENIOR:
        price = 4
        
    elif STUDENT1 <= age <= STUDENT2:
        
        student = str(input("Are you a student at this school? (Y/N): "))
    
        if student == "Y":
            price = 1
        
        else:
            price = 3
            
    elif ADULT1 <= age <= ADULT2:
        price = 5
        
    elif KID1 <= age <= KID2:
        price = 2
        
    return price













