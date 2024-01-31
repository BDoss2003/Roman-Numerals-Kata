import unittest
from roman_numerals import int_to_roman, roman_to_int

class TestRomanConversion(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(11), 'XI')
        self.assertEqual(int_to_roman(123), 'CXXIII')
        # Add more test cases as needed

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int('XI'), 11)
        self.assertEqual(roman_to_int('CXXIII'), 123)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
