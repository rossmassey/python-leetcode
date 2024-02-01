from typing import Optional, List, Dict

class Solution0217:
    """
    `Easy <https://leetcode.com/problems/contains-duplicate/>`_
    -----------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= nums.length <= 10^5``
        * ``-10^9 <= nums[i] <= 10^9``

    Given an integer array ``nums``, return ``True`` if any value appears **at
    least twice** in the array, and return ``False`` if every element is
    distinct.

    ------

    :Example 1:

    >>> Solution0217.containsDuplicate(nums = [1,2,3,1])
    True


    :Example 2:

    >>> Solution0217.containsDuplicate(nums = [1,2,3,4])
    False


    :Example 3:

    >>> Solution0217.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
    True

    """
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        """
        Args:
            nums (List[int]): list to check for duplicate
        Returns:
            bool: if a duplicate was found

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            add each number to a set as iterate through

            if a number was seen previously (in the set), it is duplicate

        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        
