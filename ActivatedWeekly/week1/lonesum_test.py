import unittest

from lone_sum import lone_sum

class LoneSumTests(unittest.TestCase):

    def test_no_repeated_parameter(self):
        self.assertEqual(6, lone_sum(1,2,3))

    def test_repeated_parameters(self):
        self.assertEqual(2, lone_sum(3, 2, 3))

    def test_all_repeated_parameters(self):
        self.assertEqual(0, lone_sum(3,3,3))

if __name__ == '__main__':
    unittest.main()
