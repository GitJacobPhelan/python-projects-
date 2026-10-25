
"""Unit tests for the text analyser."""

import unittest

from text_analyser import get_word_frequencies


class TestWordFrequencies(unittest.TestCase):
    """Tests for word-frequency calculations."""

    def test_counts_words(self):
        """Test that individual words are counted."""
        result = get_word_frequencies("hello world")
        expected = {"hello": 1, "world": 1}

        self.assertEqual(result, expected)

    def test_counts_repeated_words(self):
        """Test that repeated words have the correct frequency."""
        result = get_word_frequencies("cat cat dog")
        expected = {"cat": 2, "dog": 1}

        self.assertEqual(result, expected)

    def test_ignores_capitalisation(self):
        """Test that capitalisation does not affect word frequency."""
        result = get_word_frequencies("Python python PYTHON")
        expected = {"python": 3}

        self.assertEqual(result, expected)

    def test_strips_surrounding_punctuation(self):
        """Test that surrounding punctuation is removed."""
        result = get_word_frequencies("(hello), hello!")
        expected = {"hello": 2}

        self.assertEqual(result, expected)

    def test_empty_text(self):
        """Test that empty text returns an empty dictionary."""
        result = get_word_frequencies("")

        self.assertEqual(result, {})

    def test_punctuation_only(self):
        """Test that punctuation-only input produces no words."""
        result = get_word_frequencies("!!! ??? ...")

        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
