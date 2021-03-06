def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    word = word.lower()
    return word.count(letter)

sequences = [('Hello World', 'h'), ('Hello World', 'z'), ('Hello World', 'l')]

for word, letter in sequences:
    print(single_letter_count(word, letter))