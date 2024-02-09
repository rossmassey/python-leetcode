from typing import Optional, List, Dict

class Solution0015:
    """
    `Medium <https://leetcode.com/problems/3sum/>`_
    -----------------------------------------------

    .. sidebar:: Constraints

        * ``3 <= nums.length <= 3000``
        * ``-10^5 <= nums[i] <= 10^5``

    Given an integer array nums, return all the triplets ``[nums[i], nums[j], nums[k]]``
    such that ``i != j``, ``i != k``, and ``j != k``, and ``nums[i] + nums[j] + nums[k] == 0``.

    Notice that the solution set must not contain duplicate triplets.

    ------

    :Example 1:

    >>> Solution0015.threeSum(nums = [-1,0,1,2,-1,-4])
    [[0, 1, -1], [-1, 2, -1]]

    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

    The distinct triplets are [-1,0,1] and [-1,-1,2].

    Notice that the order of the output and the order of the triplets does not matter.


    :Example 2:

    >>> Solution0015.threeSum(nums = [0,1,1])
    []

    The only possible triplet does not sum up to 0.


    :Example 3:

    >>> Solution0015.threeSum(nums = [0,0,0])
    [[0, 0, 0]]

    The only possible triplet sums up to 0.

    """
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        """
        Args:
            nums (List[int]): nums to search
        Returns:
            List[List[int]]: triplets that sum to zero

        ------

        :Runtime:   ``O(n^2)``
        :Space:     ``O(n)``

        :Strategy:

            use a ``set`` to handle duplicates

            for each ``outer_num``, use two pointers on other nums (towards
            right to skip ones already seen) to find two that add up to
            ``-outer_num``, which combined will be ``0``

            ``sort`` nums so can increment ``left`` pointer to increase sum, and
            decrement ``right`` pointer to decrease it

        """
        # use set to handle duplicates
        triplets = set()
        sorted_nums = sorted(nums)

        for i, outer_num in enumerate(sorted_nums):
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                triplet = (sorted_nums[left], sorted_nums[right], outer_num)
                triplet_sum = sum(triplet)

                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    triplets.add(triplet)
                    right -= 1
                    left += 1
            
        return [list(triplet) for triplet in triplets]
