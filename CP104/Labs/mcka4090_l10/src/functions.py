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

#--------Question4--------#
def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    line = fh.readline().strip()
    result = line.split(',')

    while line != "":
        
        if line.split(',')[-1] < result[-1]:
            
            result = line.split(',')

        line = fh.readline().strip()

    return result

#--------Question7--------#
def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    num = None
    line = fh.readline().strip()
    
    while line != "":
        
        n = int(line)
        
        if not num or n > num:
            
            num = n 
            
        line = fh.readline().strip()
    
    fh.write(f"\n{num}")
    
    return num

#--------Question10--------#
def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    
    count = 0
    line = fh.readline()
    
    while line !="":
        
        line = line.strip()
        
        if word == line:
            
            count += 1
            
        line = fh.readline()
        
    return count

#--------Question11--------#
def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline().strip()
    word = line
    
    while line != "":
        
        if len(line) >= len(word):
            
            word = line
            
        line = fh.readline().strip()
        
    return word

#--------Question13--------#
def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()
    
    while line != "":
        
        fh_2.write(line)
        
        line = fh_1.readline()
        
    return












































