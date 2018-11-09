def longest_palindrome(word):
    """A method that accepts a word as an argument, evaluates each letter in the word,
    returns the len of the palindrome if it exists"""

    hash_set = set()

    for letter in word:
        if letter not in  hash_set:
            hash_set.add(letter)
        else:
            hash_set.remove(letter)

    return len(word) - len(hash_set) + 1 if len(hash_set) > 0 else len(word)
