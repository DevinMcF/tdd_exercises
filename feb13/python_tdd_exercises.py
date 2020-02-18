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
    return [word for word in s.split(' ')][[len(word) for word in s.split(' ')].index(max([len(word) for word in s.split(' ')]))]


def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    chars = ('a', 'c', 't', 'g')
    return all(ch.lower() in chars for ch in s)


def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    pairs = {"a": "t",
             "t": "a",
             "c": "g",
             "g": "c"}
    try:
        return pairs[c.lower()]
    except:
        return "unknown"


def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    return s.upper().replace('T', "U")


def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    pairs = {"A": "T",
             "T": "A",
             "C": "G",
             "G": "C"}
    return ''.join([pairs[ch] for ch in s.upper()])


def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    pairs = {"A": "T",
             "T": "A",
             "C": "G",
             "G": "C"}
    return ''.join([pairs[ch] for ch in s.upper()])[::-1]


def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    return string.replace(substring, '')


def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    return [pos for pos, trip in enumerate([dna[i:i + 3] for i in range(0, len(dna), 3)]) if trip == triplet]


def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    return sorted(set([(tri, sum([[s[i:i + 3] for i in range(x, len(s), 3) if len(s[i:i + 3]) == 3] for x in range(3)], []).count(tri)) for tri in sum([[s[i:i + 3] for i in range(x, len(s), 3) if len(s[i:i + 3]) == 3] for x in range(3)], [])]))


def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    return None