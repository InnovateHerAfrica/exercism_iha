import unittest

from sequence import sequence

class Sequeunce_Tests(unittest.TestCase):

        def test_mid_sequence(self):
            self.assertEqual(True, sequence([1, 1, 2, 3, 1], [1 ,2, 3]))
        def test_end_sequence(self):
            self.assertEqual(True, sequence([1, 1, 2, 1, 2, 3],[1, 2, 3] ))
        def test_no_sequence(self):
            self.assertEqual(False, sequence([1, 1, 2, 4, 1],[1, 2, 3] ))

if __name__ == '__main__':
    unittest.main()
