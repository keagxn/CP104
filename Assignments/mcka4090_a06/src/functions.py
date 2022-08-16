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
def winner():
    """
    -------------------------------------------------------
    Returns the team count for both teams
    Use: winner()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        team1_count, team2_count
    -------------------------------------------------------
    """
    game_winner = input("Enter the winning team: ")
    win = game_winner
    team1_count = 0
    team2_count = 0
    
    if game_winner != "":
        
        team1_count = team1_count + 1
        
    while game_winner != "":
        
        game_winner = input("Enter the winning team: ")
        
        if win == game_winner:
            
            team1_count = team1_count + 1
            
        elif win != game_winner and game_winner != "":
            
            team2_count = team2_count + 1
    
    return team1_count, team2_count

#--------Question2--------#
def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    i = 2
    
    while prime == True and i < num:
        
        if num % i == 0:
            
            prime = False
            
        else:
            
            i = i + 1
            
    return prime

#--------Question3--------#
def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'Principal: ${principal:0.2f}')
    print(f'Interest Rate: %.{rate:0.2f}')
    print(f'Monthly Payment: ${payment:0.2f}')

    print('-' * 34)
    print('%5s %10s %10s %12s' % ('Month', 'Interest', 'Payment', 'Balance'))
    print('-' * 34)

    month = 1
    rate = rate / 1200

    while principal > 0:
        
        interest_paid = principal * rate
        principal_paid = payment - interest_paid

        if principal - principal_paid < 0:
            
            if principal < payment:
                
                payment = principal + interest_paid
                
            principal = 0
            
        else:
            
            principal -= principal_paid

        print(f'{month:5d}',f'{interest_paid:10.2f}', f'{payment:10.2f}', f'{principal:12.2f}')

        month += 1
        
    return

#--------Question4--------#
def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 1
    
    while abs(num) >= 10 :
        
        num /= 10
        count += 1
    
    return count

#--------Question5--------#
def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    current_num = 1

    while current_num <= num // 2:
        
        if num % current_num == 0:
            
            total += current_num

        current_num += 1
        
    return total















