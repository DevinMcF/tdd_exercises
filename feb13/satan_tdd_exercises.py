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
    return c.lower() in ('a', 'e', 'i', 'o', 'u', 'y')


def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    return len([ch for ch in s if ch in ('a', 'e', 'i', 'o', 'u', 'y')])


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
    return all(ch.lower() in ('a', 'c', 't', 'g') for ch in s)


def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    try:
        return {"a": "t", "t": "a", "c": "g", "g": "c"}[c.lower()]
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
    return ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[ch] for ch in s.upper()])


def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    return ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[ch] for ch in s.upper()])[::-1]


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
    return [float(ch[column_number - 1].replace(' ', '')) for ch in [ch.split('  ') for ch in open(file_name, 'r').read().replace('    ', '').split('\n')]]


def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant but present character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    return {open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')}[max({open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')})], {open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')}[min({open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')})]


def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    lst = []
    [[[lst.append((a, b, c)) for a in range(1, b) if a * a + b * b == c * c] for b in range(1, c)] for c in range(1, n + 1)]
    return lst

