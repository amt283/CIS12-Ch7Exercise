"""write a version of uses_all that calls uses_only."""

def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """

    for letter in word:
        if letter not in available:
            return False
    return True


def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('mississippi', 'misp')
    True
    """
    if not uses_only(word, required):
            return False
    return True

