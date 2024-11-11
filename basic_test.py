def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    x = 7
    y = 2
    div = x // 2
    return div
int_division()

def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    j = 3.0
    h = 2
    mult = j*h
    return mult
float_multiplication()

def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    y = int_division() + float_multiplication()
    return y

combine_operations()


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    
    string = 'Python is awesome!'
    for i in string:
        if i == '!':
            i.remove()
        print(i)
    # new_string = string.split()
    # print(new_string)
    # for i in new_string:
    #     print(i)
    pass
print(extract_word())

def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    low_string = string.lower()
    return low_string
to_lowercase()

def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    count = 0
    string = 'Python is awesome!'
    for i in string:
        if i == 'o':
            count += 1

    return count
count_o()

def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    return False
evaluate_boolean()
