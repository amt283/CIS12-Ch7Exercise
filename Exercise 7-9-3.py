"""Write a function called uses_only that takes a word and a string of letters, and that returns True if the word
contains only letters in the string.

Here’s an outline of the function that includes two doctests. Fill in the function so it passes these tests, and add
at least one more doctest."""


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