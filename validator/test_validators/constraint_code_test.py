import unittest
from validator import constraint_codes as cc

class TestValidatorFunctions(unittest.TestCase):

    def test_is_anagram(self):
        # Test for success
        text = "listen"
        reference = "silent"
        result = cc.is_anagram(text, reference)
        self.assertTrue(result)

        # Test for failure
        text = "listen"
        reference = "silence"
        result = cc.is_anagram(text, reference)
        self.assertFalse(result)

    def test_is_plaindrome(self):
        # Test for success
        text = "madam"
        result = cc.is_plaindrome(text)
        self.assertTrue(result)

        # Test for failure
        text = "hello"
        result = cc.is_plaindrome(text)
        self.assertFalse(result)

    def test_end_start_with(self):
        # Test for success
        text = "Hello"
        position = "start"
        letter = "H"
        result = cc.end_start_with(text, position, letter)
        self.assertTrue(result)

        # Test for failure
        text = "Hello"
        position = "end"
        letter = "H"
        result = cc.end_start_with(text, position, letter)
        self.assertFalse(result)

    def test_initials_make_up(self):
        # Test for success
        text = "Hello World"
        reference = "hw"
        result = cc.initials_make_up(text, reference)
        self.assertTrue(result)

        # Test for failure
        text = "Hello World"
        reference = "wh"
        result = cc.initials_make_up(text, reference)
        self.assertFalse(result)

    def test_count_words(self):
        # Test for success
        text = "Hello World"
        required = 2
        comparator = 'exactly'
        result = cc.count_words(text, required, comparator)
        self.assertTrue(result)

        # Test for failure
        text = "Hello World"
        required = 3
        comparator = 'exactly'
        result = cc.count_words(text, required, comparator)
        self.assertFalse(result)

    def test_count_word_appearance(self):
        # Test for success
        text = "Hello World Hello"
        word = "Hello"
        number = 2
        comparator = 'exactly'
        result = cc.count_word_appearance(text, word, number, comparator)
        self.assertTrue(result)

        # Test for failure
        text = "Hello World Hello"
        word = "Hello"
        number = 3
        comparator = 'exactly'
        result = cc.count_word_appearance(text, word, number, comparator)
        self.assertFalse(result)

    def test_check_sentence_count(self):
        # Test for success
        text = "Hello. World."
        expected_count = 2
        comparator = 'exactly'
        result = cc.check_sentence_count(text, expected_count, comparator)
        self.assertTrue(result)

        # Test for failure
        text = "Hello. World."
        expected_count = 3
        comparator = 'exactly'
        result = cc.check_sentence_count(text, expected_count, comparator)
        self.assertFalse(result)

    def test_check_letters(self):
        # Test for success
        text = "Hello"
        letters = ["H", "e"]
        result = cc.check_letters(text, letters)
        self.assertTrue(result)

        # Test for failure
        text = "Hello"
        letters = ["x", "y"]
        result = cc.check_letters(text, letters)
        self.assertFalse(result)

    def test_constraint_empty(self):
        # Test for success
        text = "Hello"
        result = cc.constraint_empty(text)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()