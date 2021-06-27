from itertools import count


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWELS = 'aeiou'
    counter = {}

    for letter in phrase:
        counter[letter.lower()] = counter.get(letter.lower(), 0) + 1
    
    return {k:v for k, v in counter.items() if k in VOWELS}


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))