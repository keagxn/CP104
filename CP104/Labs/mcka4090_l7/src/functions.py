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

#--------Question1--------#
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    
    number = randint(1, high)
    guess = int(input("Guess: "))
    count = 1
    
    while guess != number:
        
        if guess > number:
            
            print("Too high, try again.")
            
        else:
            
            print("Too low, try again.")
            
        guess = int(input("Guess: "))
        count += 1
    
    print(f"Congratulations - good guess!")
    
    return count

#--------Question2--------#
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 0
    
    while 2**power < target:
        power += 1
        
    return 2**power

#--------Question5--------#
def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    value = float(input("First positive value: "))
    
    total = 0
    minimum = value
    maximum = value
    total_values = 0
    
    while value >= 0:
        
        total += value 
        total_values += 1
        
        if value > maximum:
            
            maximum = value
            
        elif value < minimum:
            
            minimum = value
        
        value = float(input("Next positive value: "))
    
    average = total/total_values
    
    return minimum, maximum, total, average

#--------Question8--------#
def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    
    spent = float(input("Enter an expense (0 to quit): $"))
    
    expenses = spent
    
    while spent != 0:
        
        spent = float(input("Enter another expense (0 to quit): $"))
        expenses += spent
        
    balance = available - expenses
    
    if balance < 0:
        status = "Deficit"
    
    elif balance > 0:
        status = "Surplus"
        
    else:
        status = "Balanced"
        
    return expenses, balance, status
    
#--------Question10--------#
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    TAX = 0.03625
    OVERTIME_RATE = 1.5
    OVERTIME = 40
    
    total = 0
    employees = 0
    emp_id = int(input("Employee ID: "))
    
    while emp_id != 0:
        wage = float(input("Hourly wage rate: "))
        hours = float(input("Hours worked: "))
        
        if hours > OVERTIME:
            over_time = hours - OVERTIME
        else:
            over_time = 0
            
        net = ((wage*(hours - over_time)) + (wage*over_time*OVERTIME_RATE)) * (1 - TAX)
        
        print(f"Net payment for employee {emp_id}: ${net:,.2f}")
        print()
        
        emp_id = int(input("Employee ID: "))
        
        total += net
        employees += 1
        
    average = total/employees
    
    return total, average

















