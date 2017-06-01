import unittest

from prime_factor import largest_prime_factor

class PrimeFactorTests(unittest.TestCase):

        def test_small_number(self):
            self.assertEqual(29, largest_prime_factor(13195))

if __name__ == '__main__':
        unittest.main()
