"""Write a function called uses_all that takes a word and a string of letters, and that returns True if the word
contains all of the letters in the string at least once."""


def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('mississippi', 'misp')
    True
    """
    for letter in required:
        if letter not in word:
            return False
    return True
