def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    if len(str(num1)) != len(str(num2)):
        return False

    num1, num2 = str(num1), str(num2)
    setnum1 = sorted(list(set(num1)))
    setnum2 = sorted(list(set(num2)))

    return "".join(setnum1) == "".join(setnum2)

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))