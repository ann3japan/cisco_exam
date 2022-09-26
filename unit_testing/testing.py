import unittest
from sample import factors 
from sample import is_prime 
from sample import vowels 

class TestMain(unittest.TestCase):

    def test_vowels(self):
        self.assertEqual(vowels("hello"), ['e','o'])
        self.assertEqual(vowels("world"), ['o'])

    def test_factors(self):
        self.assertEqual(factors(7), [7])
        self.assertEqual(factors(6), [2, 3])

    def test_is_prime(self):
        self.assertTrue(is_prime(19))
        self.assertFalse(is_prime(18))

    def test_isupper(self):
        self.assertTrue('ANNA'.isupper())
        self.assertFalse('Anna'.isupper())
    
if __name__ == '__main__':
    unittest.main()