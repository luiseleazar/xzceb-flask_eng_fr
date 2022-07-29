"""Tests for translator.py"""
import unittest
import sys

sys.path.append('..')

from machinetranslation.translator import english_to_french, french_to_english

class test_translator(unittest.TestCase):
    def test_english_to_french(self):
        result = english_to_french("Hello")
        return self.assertEqual("Bonjour", result)
    
    def test_null_english_to_french(self):
        result = english_to_french("")
        return self.assertEqual("", result)
    
    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        return self.assertEqual("Hello", result)

    def test_null_french_to_english(self):
        result = french_to_english("")
        return self.assertEqual("", result)

if __name__ == '__main__':
    unittest.main()
