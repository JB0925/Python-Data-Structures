def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase = phrase.split()
    return phrase[0].title() if len(phrase) == 1 \
            else f'{phrase[0].title()} {" ".join(phrase[1:])}'

print(capitalize('python'))
print(capitalize('only first word'))