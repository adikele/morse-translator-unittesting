'''
Test program to test functions in morsetranslator_v1.py
'''

import unittest
from morsetranslator_v1 import encodetomorse, decodemorse


class EncodeTestCase(unittest.TestCase):
    """Tests for encoder function.py"""

    def test_is_encodingEx1Right(self):
        """Is encodetomorse function coded correctly?"""
        self.assertEqual(encodetomorse("sos SOS. s-s SO-"),
                         ("... --- ...  ... --- ... .-.-.-  ... <CNF> ...  ... --- <CNF>"),
                         'encoding not correct')

    def test_is_encodingEx2Right(self):
        """Is encodetomorse function coded correctly?"""
        self.assertEqual(encodetomorse(""), (""), 'encoding not correct')

    def test_is_encodingEx3Right(self):
        """Is encodetomorse function coded correctly?"""
        self.assertEqual(encodetomorse(" "), ("<CNF>"), 'encoding not correct')


class DecodeTestCase(unittest.TestCase):
    """Tests for decoder function.py"""

    def test_is_decodingEx1Right(self):
        """Is decodemorse coded correctly?"""
        self.assertEqual(decodemorse("... -  ..- ...-"), ("ST UV"),
                         'decoding not correct')

    def test_is_decodingEx2Right(self):
        """Is decodemorse coded correctly?"""
        self.assertEqual(decodemorse("... ----  ..- ...-"), ("S<CNF> UV"),
                         'decoding not correct')


if __name__ == '__main__':
    unittest.main()
