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
def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 1
    line = fh.readline().strip()
    
    while count <= linecount and line != "":
        
        print(f"{line}")

        line = fh.readline().strip()
        count += 1

    return

#--------Question2--------#
def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    
    for line in fh:
        line = line.strip().split(',')
        
        for node in line:
            
            if node.isdigit():
                numbers.append(int(node))

    return numbers

#--------Question3--------#
def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0

    for line in fh:
        
        for ch in line:
            
            if ch.isupper():
                ucount += 1
                
            elif ch.islower():
                lcount += 1
                
            elif ch.isdigit():
                dcount += 1
                
            elif ch.isspace():
                wcount += 1

    return ucount, lcount, dcount, wcount

#--------Question4--------#
def flatten(matrix):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list matrix. A 'flattened' list is a
    2D list that is converted into a 1D list by rows.
    matrix must be unchanged.
    Use: flat = matrix_flatten(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of int)
    Returns:
        flat - the flattened version of matrix (list of int)
    -------------------------------------------------------
    """
    flat = []

    for row in range(len(matrix)):
        
        for col in range(len(matrix[0])):
            flat.append(matrix[row][col])

    return flat

#--------Question5--------#
def matrix_rotate_right(matrix):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: rotated = matrix_rotate_right(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2d list of int/float)
    Returns:
        rotated - the rotated version of matrix (2D list of int/float)
    -------------------------------------------------------
    """
    rotated = []
    
    for i in range(len(matrix[0])):
        rotated.append([])
        
        for j in range(len(matrix) - 1, -1, -1):
            rotated[i].append(matrix[j][i])

    return rotated

#--------Question6--------#
def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        name
        street
        city
        postal code
        --
    Each address in the list of addresses is a list of the form:
    [name, street, city, postal code]
    Use: addresses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        addresses - the addresses from fh (list of str)
    -------------------------------------------------------
    """
    addresses = []

    line = fh.readline()
    address = [line.strip()]

    for line in fh:
        line = line.strip()

        if line != "--":
            address.append(line)
            
        else:
            addresses.append(address)
            address = []

    return addresses





































