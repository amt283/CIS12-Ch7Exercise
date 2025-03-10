"""Write a function called check_word that checks whether a given word is acceptable. It should take as parameters the
word to check, a string of seven available letters, and a string containing the single required letter. You can use
the functions you wrote in previous exercises.

According to the “Spelling Bee” rules,
- Four-letter words are worth 1 point each.
- Longer words earn 1 point per letter.
- Each puzzle includes at least one “pangram” which uses every letter. These are worth 7 extra points!

Write a function called score_word that takes a word and a string of available letters and returns its score. You can
assume that the word is acceptable."""

def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """

    # Checks if word only uses letters available
    uses_avail = uses_only(word,available.lower())

    if len(word) < 4:
        return False
    elif uses_avail and (required.lower() in word):
        return True
    elif not uses_only(word, available):
        return False

def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    # Start with the base score (length of the word)
    score = 0
    word_len = len(word)

    if word_len == 4:
        score = 1
    elif word_len > 4:
        score += word_len

    # If it's a pangram, add 7 points
    if uses_all(word,available.lower()):
        score += 7

    return score

def uses_all(word, required):
    """Returns True if all letters in letter_search (allowing repeats) are found in word.
    >>> uses_all('fish', 'abcdijk')
    False
    >>> uses_all('fantastic', 'afstic')
    True
    """
    # Count the occurrences of each character in s2
    for letter in required:
        if letter not in word:
            return False
    return True

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

# print(check_word('color', 'ACDLORT', 'R'))   # True
# print(word_score('color', 'ACDLORT'))        # 5
# print(check_word('cartload', 'ACDLORT', 'R'))  # True
# print(word_score('cartload', 'ACDLORT'))      # 15