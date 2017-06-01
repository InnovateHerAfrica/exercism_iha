import unittest
from squirrels import cigar_party

class TestSqurriels(unittest.TestCase):

    def test_cigar_party_out_of_range_non_weekend(self):
        # cigars shouldn't be less than 40
        self.assertEqual(cigar_party(30, False), False)

    def test_cigar_party_in_range_on_a_non_weekend(self):
        # should return True
        self.assertEqual(cigar_party(50, False), True)

    def test_cigar_party_out_of_upper_range_weekend(self):
        # should return True
        self.assertEqual(cigar_party(70, True), True)


if __name__ == '__main__':
    unittest.main()
