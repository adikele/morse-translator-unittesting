'''
Test program to test functions in morsetranslator_v2.py program file

OUTPUT:
.....
----------------------------------------------------------------------
Ran 5 tests in 0.009s

OK

COMMENTS:
3.9.18
1. All 5 tests pass

'''

import unittest
from morsetranslator_v2 import encodetomorse, decodemorse


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
