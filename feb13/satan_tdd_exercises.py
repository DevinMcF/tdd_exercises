def reverse_list(lst):
    return lst[::-1]


def reverse_string(s):
    return s[::-1]


def is_english_vowel(c):
    return c.lower() in ('a', 'e', 'i', 'o', 'u', 'y')


def count_num_vowels(s):
    return len([ch for ch in s if ch in ('a', 'e', 'i', 'o', 'u', 'y')])


def histogram(lst):
    return ''.join(['#' * num + "\n" for num in lst])[:-1]


def get_word_lengths(s):
    return [len(word) for word in s.split(' ')]


def find_longest_word(s):
    return [word for word in s.split(' ')][[len(word) for word in s.split(' ')].index(max([len(word) for word in s.split(' ')]))]


def validate_dna(s):
    return all(ch.lower() in ('a', 'c', 't', 'g') for ch in s)


def base_pair(c):
    try:
        return {"a": "t", "t": "a", "c": "g", "g": "c"}[c.lower()]
    except:
        return "unknown"


def transcribe_dna_to_rna(s):
    return s.upper().replace('T', "U")


def get_complement(s):
    return ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[ch] for ch in s.upper()])


def get_reverse_complement(s):
    return ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[ch] for ch in s.upper()])[::-1]


def remove_substring(substring, string):
    return string.replace(substring, '')


def get_position_indices(triplet, dna):
    return [pos for pos, trip in enumerate([dna[i:i + 3] for i in range(0, len(dna), 3)]) if trip == triplet]


def get_3mer_usage_chart(s):
    return sorted(set([(tri, sum([[s[i:i + 3] for i in range(x, len(s), 3) if len(s[i:i + 3]) == 3] for x in range(3)], []).count(tri)) for tri in sum([[s[i:i + 3] for i in range(x, len(s), 3) if len(s[i:i + 3]) == 3] for x in range(3)], [])]))


def read_column(file_name, column_number):
    return [float(ch[column_number - 1].replace(' ', '')) for ch in [ch.split('  ') for ch in open(file_name, 'r').read().replace('    ', '').split('\n')]]


def character_statistics(file_name):
    return {open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')}[max({open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')})], {open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')}[min({open(file_name, 'r').read().lower().count(ch): ch for ch in open(file_name, 'r').read().lower() if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')})]


def pythagorean_triples(n):
    lst = []
    [[[lst.append((a, b, c)) for a in range(1, b) if a * a + b * b == c * c] for b in range(1, c)] for c in range(1, n + 1)]
    return lst

