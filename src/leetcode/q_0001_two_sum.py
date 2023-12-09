from typing import List, Dict


class Solution0001:
    """
    `Easy <https://leetcode.com/problems/two-sum/>`_
    ------------------------------------------------

    .. sidebar:: Constraints

        * ``2 <= len(nums) <= 10^4``
        * ``-10^9 <= nums[i] <= 10^9``
        * ``-10^9 <= target <= 10^9``
        * Only one valid answer exists.

    Given an array of integers ``nums`` and an integer ``target``, return indices of
    the two numbers such that they add up to ``target``.

    You may assume that each input would have **exactly one solution**, and you may
    not use the same element twice. You can return the answer in any order.

    :Example:

    >>> Solution0001.two_sum([2, 7, 11, 15], 9)
    [1, 0]

    """
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums (List[int]): List of integers.
            target (int): The target sum.

        Returns:
            List[int]: Indices of the two numbers that add up to the target.

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            use ``indexOfComplements`` to track complements (``target`` - ``num``)
            and their indices

            while iterating ``nums``, if ``num`` is in the dictionary, return its
            ``index`` and ``otherIndex`` from the dictionary

            giving two indices adding to ``target``

        """
        index_of_complements: Dict[int, int] = {}

        for index, num in enumerate(nums):
            if num in index_of_complements:
                return [index, index_of_complements[num]]
            index_of_complements[target - num] = index

        return [-1, -1]
