import unittest
from sample import factors 
from sample import is_prime 
from sample import vowels 

class TestMain(unittest.TestCase):

    def test_vowels(self):
        self.assertEqual(vowels("hello"), ['e','o'])
        self.assertEqual(vowels("world"), ['o'])

    def test_factors(self):
        self.assertEqual(factors(5), [5])

    def test_is_prime(self):
        self.assertTrue(is_prime(19))
        self.assertFalse(is_prime(18))

    def test_len(self):
        self.assertEqual(len([1,2, 3, 4, 5]), 5)
    
if __name__ == '__main__':
    unittest.main()
