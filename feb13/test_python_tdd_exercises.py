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

    def test_base_pair(self):
        self.assertEqual(base_pair('a'), 't')
        self.assertEqual(base_pair('t'), 'a')
        self.assertEqual(base_pair('c'), 'g')
        self.assertEqual(base_pair('g'), 'c')
        self.assertEqual(base_pair('A'), 't')
        self.assertEqual(base_pair('T'), 'a')
        self.assertEqual(base_pair('C'), 'g')
        self.assertEqual(base_pair('G'), 'c')
        self.assertEqual(base_pair('x'), 'unknown')
        self.assertEqual(base_pair('foo'), 'unknown')

    def test_transcribe_dna_to_rna(self):
        dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
        self.assertEqual(transcribe_dna_to_rna(dna), 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG')

    def test_get_complement(self):
        self.assertEqual(get_complement('CCGGAAGAGCTTACTTAG'), 'GGCCTTCTCGAATGAATC')
        self.assertEqual(get_complement('ccggaagagcttacttag'), 'GGCCTTCTCGAATGAATC')

    def test_get_reverse_complement(self):
        self.assertEqual(get_reverse_complement('CCGGAAGAGCTTACTTAG'), 'CTAAGTAAGCTCTTCCGG')
        self.assertEqual(get_reverse_complement('ccggaagagcttacttag'), 'CTAAGTAAGCTCTTCCGG')

    def test_remove_substring(self):
        self.assertEqual(remove_substring('GAA', 'CCGGAAGAGCTTACTTAG'), 'CCGGAGCTTACTTAG')
        self.assertEqual(remove_substring('CCG', 'CCGGAAGAGCTTACTTAG'), 'GAAGAGCTTACTTAG')
        self.assertEqual(remove_substring('TAG', 'CCGGAAGAGCTTACTTAG'), 'CCGGAAGAGCTTACT')
        self.assertEqual(remove_substring('GAA', 'GAAGAAGAA'), '')

    def test_get_position_indices(self):
        self.assertEqual(get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG'), [1])
        self.assertEqual(get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA'), [1, 6, 7])

    def test_get_3mer_usage_chart(self):
        s = 'CCGGAAGAGCTTACTTAGGAAGAA'
        result = []
        result.append(('AAG', 2))
        result.append(('ACT', 1))
        result.append(('AGA', 2))
        result.append(('AGC', 1))
        result.append(('AGG', 1))
        result.append(('CCG', 1))
        result.append(('CGG', 1))
        result.append(('CTT', 2))
        result.append(('GAA', 3))
        result.append(('GAG', 1))
        result.append(('GCT', 1))
        result.append(('GGA', 2))
        result.append(('TAC', 1))
        result.append(('TAG', 1))
        result.append(('TTA', 2))
        self.assertEqual(get_3mer_usage_chart(s), result)

    def test_read_column(self):
        import tempfile
        import os

        text = """1   0.1  0.001
    2   0.2  0.002
    3   0.3  0.003
    4   0.4  0.004
    5   0.5  0.005
    6   0.6  0.006"""

        # we save this text to a temporary file
        file_name = tempfile.mkstemp()[1]
        with open(file_name, 'w') as f:
            f.write(text)

        # and now we pass the file name to the function which will read the column
        self.assertEqual(read_column(file_name, 2), [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

        # we remove the temporary file
        os.unlink(file_name)

    def test_character_statistics(self):
        import tempfile
        import os

        text = """
    To be, or not to be: that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles,
    And by opposing end them? To die: to sleep;
    No more; and by a sleep to say we end
    The heart-ache and the thousand natural shocks
    That flesh is heir to, 'tis a consummation
    Devoutly to be wish'd. To die, to sleep;
    To sleep: perchance to dream: ay, there's the rub;
    For in that sleep of death what dreams may come
    When we have shuffled off this mortal coil,
    Must give us pause: there's the respect
    That makes calamity of so long life;
    For who would bear the whips and scorns of time,
    The oppressor's wrong, the proud man's contumely,
    The pangs of despised love, the law's delay,
    The insolence of office and the spurns
    That patient merit of the unworthy takes,
    When he himself might his quietus make
    With a bare bodkin? who would fardels bear,
    To grunt and sweat under a weary life,
    But that the dread of something after death,
    The undiscover'd country from whose bourn
    No traveller returns, puzzzles the will
    And makes us rather bear those ills we have
    Than fly to others that we know not of?
    Thus conscience does make cowards of us all;
    And thus the native hue of resolution
    Is sicklied o'er with the pale cast of thought,
    And enterprises of great pith and moment
    With this regard their currents turn awry,
    And lose the name of action.--Soft you now!
    The fair Ophelia! Nymph, in thy orisons
    Be all my sins remember'd."""

        # we save this text to a temporary file
        file_name = tempfile.mkstemp()[1]
        with open(file_name, 'w') as f:
            f.write(text)

        # and now we pass the file name to the function which will get the stats
        self.assertEqual(character_statistics(file_name), ('e', 'q'))

        # we remove the temporary file
        os.unlink(file_name)

    def test_pythagorean_triples(self):
        self.assertEqual(pythagorean_triples(5), [(3, 4, 5)])
        self.assertEqual(pythagorean_triples(15), [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)])
        pass  # so far we do not test anything, check also test coverage