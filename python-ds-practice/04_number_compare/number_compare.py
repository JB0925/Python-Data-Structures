def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        return 'Numbers are equal'
    elif a > b:
        return 'First is greater'
    else:
        return 'Second is greater'

print(number_compare(3, 3))
print(number_compare(3, 7))
print(number_compare(3, 1))