def reverse_list(lst):
    """
    Reverses order of elements in list lst.
    """
    return lst[::-1]


def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    return s[::-1]


def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    return c.lower() in vowels


def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    return len([ch for ch in s if ch in vowels])


def histogram(lst):
    """
    Converts a list of integers into a simple string histogram.
    """
    return ''.join(['#' * num + "\n" for num in lst])[:-1]


def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return [len(word) for word in s.split(' ')]


def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    lengths = {}
    for word in s.split(' '):
        if len(word) in lengths:
            pass
        else:
            lengths[len(word)] = word
    return lengths.get(max(lengths))


def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    chars = ('a', 'c', 't', 'g')
    return all(ch.lower() in chars for ch in s)
