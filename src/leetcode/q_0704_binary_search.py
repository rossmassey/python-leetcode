from typing import Optional, List, Dict

class Solution0704:
    """
    `Easy <https://leetcode.com/problems/binary-search/>`_
    ------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= nums.length <= 10^4``
        * ``-10^4 < nums[i], target < 10^4``
        * All the integers in ``nums`` are **unique**.
        * ``nums`` is sorted in ascending order.

    Given an array of integers ``nums`` which is sorted in ascending order, and
    an integer ``target``, write a function to search ``target`` in ``nums``.
    If ``target`` exists, then return its index. Otherwise, return ``-1``.

    You must write an algorithm with ``O(log n)`` runtime complexity.

    ------

    :Example 1:

    >>> Solution0704.search(nums = [-1,0,3,5,9,12], target = 9)
    4

    9 exists in nums and its index is 4


    :Example 2:

    >>> Solution0704.search(nums = [-1,0,3,5,9,12], target = 2)
    -1

    2 does not exist in nums so return -1

    """
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
        Args:
            nums (List[int]): nums to search
            target (int): target num
        Returns:
            int: index of target num

        ------

        :Runtime:   ``O(log n)``
        :Space:     ``O(1)``

        :Strategy:

            input is sorted, so can use binary search

            check the ``middle`` of the search space, if it is greater than
            ``target`` then update ``upper_bound`` to the left of it, if it
            is less than ``target`` then update ``loer_bound`` to the right of it

            if ``middle`` is the ``target``, return its index

        """
        
        lower_bound = 0
        upper_bound = len(nums) - 1
        
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2

            if nums[middle] > target:
                upper_bound = middle - 1
            elif nums[middle] < target:
                lower_bound = middle + 1
            else:
                return middle

        # not found
        return -1
