'''
Test program to test functions in morsetranslation_v3.py program file

OUTPUT:
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK

COMMENTS:
4.10.19
1. All 4 tests pass

'''


import unittest
from morsetranslation_v3 import encodetomorse, decodemorse


class EncodeTestCase(unittest.TestCase):
    """Tests for encoder function.py"""

    def test_encoding_1(self):
        """Is encodetomorse function coded correctly?"""
        self.assertEqual(encodetomorse("sos SOS. s-s SO-"),
                         ("... --- .../... --- ... .-.-.-/... <CNF> .../... --- <CNF>"),
                         'encoding not correct')

    def test_encoding_2(self):
        """Is encodetomorse function coded correctly?"""
        self.assertEqual(encodetomorse("I c.a.n."), ("../-.-. .-.-.- .- .-.-.- -. .-.-.-"), 
                         'encoding not correct')



class DecodeTestCase(unittest.TestCase):
    """Tests for decoder function.py"""

    def test_decoding_1(self):
        """Is decodemorse coded correctly?"""
        self.assertEqual(decodemorse("... -/..- ...-"), ("ST UV"),
                         'decoding not correct')

    def test_decoding_2(self):
        """Is decodemorse coded correctly?"""
        self.assertEqual(decodemorse("... ----/..- ...-"), ("S<CNF> UV"),
                         'decoding not correct')


if __name__ == '__main__':
    unittest.main()
