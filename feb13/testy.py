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