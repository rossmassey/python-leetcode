import unittest
from src.leetcode import Solution0001

two_sum = Solution0001.two_sum


class TwoSumTests(unittest.TestCase):

    def test_basic_a(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = {0, 1}  # can be any order
        result = set(two_sum(nums, target))
        self.assertEqual(result, expected)

    def test_basic_b(self):
        nums = [3, 2, 4]
        target = 6
        expected = {1, 2}
        result = set(two_sum(nums, target))
        self.assertEqual(result, expected)

    def test_basic_c(self):
        nums = [3, 3]
        target = 6
        expected = {0, 1}
        result = set(two_sum(nums, target))
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
