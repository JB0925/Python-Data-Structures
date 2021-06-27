from collections import deque

def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 != 0 or parens[0] == ')':
        return False

    open_parens = '('
    close_parens = ')'
    accumulator = []

    for item in parens:
        if item == open_parens:
            accumulator.append(item)
        if item == close_parens:
            accumulator.pop()
    return len(accumulator) == 0
    

print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))