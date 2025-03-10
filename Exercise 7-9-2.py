"""Write a function named uses_none that takes a word and a string of forbidden letters, and returns True if the word
does not use any of the forbidden letters.

Here’s an outline of the function that includes two doctests. Fill in the function so it passes these tests, and add
at least one more doctest."""

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('fishsticks', 'xyz')
    True
    >>> uses_none('rumplestiltskin', 'efg')
    False
    """

    forbidden_list = list(forbidden) # convert string to list so each character is an element
    passed = True

    # loop through each letter in "word"
    for letter in word:
        # compare each letter with list element (by using "in")
        if letter in forbidden_list:
            passed = False
    return passed

# print(uses_none('banana', 'xyz')) # True
# print(uses_none('apple', 'efg')) # False
# print(uses_none('fishsticks', 'xyz')) # True
# print(uses_none('rumplestiltskin', 'efg')) # False