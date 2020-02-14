from unittest import TestCase

from feb13.python_tdd_exercises import *


class TDDExerciseSuite(TestCase):

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_reverse_string(self):
        self.assertEqual(reverse_string("foobar"), "raboof")

    def test_is_english_vowel(self):
        self.assertEqual(is_english_vowel('a'), True)
        self.assertEqual(is_english_vowel('e'), True)
        self.assertEqual(is_english_vowel('i'), True)
        self.assertEqual(is_english_vowel('o'), True)
        self.assertEqual(is_english_vowel('u'), True)
        self.assertEqual(is_english_vowel('y'), True)
        self.assertEqual(is_english_vowel('A'), True)
        self.assertEqual(is_english_vowel('E'), True)
        self.assertEqual(is_english_vowel('I'), True)
        self.assertEqual(is_english_vowel('O'), True)
        self.assertEqual(is_english_vowel('U'), True)
        self.assertEqual(is_english_vowel('Y'), True)
        self.assertEqual(is_english_vowel('k'), False)
        self.assertEqual(is_english_vowel('z'), False)
        self.assertEqual(is_english_vowel('?'), False)

    def test_count_num_vowels(self):
        sentence = "hey ho let's go"
        self.assertEqual(count_num_vowels(sentence), 5)
        # sentence = "HEY ho let's GO"
        # self.assertEqual(count_num_vowels(sentence), 5)
        # paragraph = """She told me her name was Billie Jean,
        #                as she caused a scene
        #                Then every head turned with eyes
        #                that dreamed of being the one
        #                Who will dance on the floor in the round"""
        # self.assertEqual(count_num_vowels(paragraph), 54)

    def test_histogram(self):
        self.assertEqual(histogram([2, 5, 1]), '##\n#####\n#')

    def test_get_word_lengths(self):
        text = "Three tomatoes are walking down the street"
        self.assertEqual(get_word_lengths(text), [5, 8, 3, 7, 4, 3, 6])

    def test_find_longest_word(self):
        text = "Three tomatoes are walking down the street"
        self.assertEqual(find_longest_word(text), "tomatoes")
        text = "foo foo1 foo2 foo3"
        self.assertEqual(find_longest_word(text), "foo1")

    def test_validate_dna(self):
        self.assertEqual(validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag'), True)
        self.assertEqual(validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag'), False)
        self.assertEqual(validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag'), False)
