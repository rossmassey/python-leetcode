from typing import Optional, List, Dict

class Solution0167:
    """
    `Medium <https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/>`_
    ---------------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``2 <= numbers.length <= 3 * 10^4``
        * ``-1000 <= numbers[i] <= 1000``
        * ``numbers`` is sorted in **non-decreasing order**.
        * ``-1000 <= target <= 1000``
        * The tests are generated such that there is **exactly one solution**.

    Given a **1-indexed** array of integers ``numbers`` that is already
    **sorted in non-decreasing order**, find two numbers such that they add
    up to a specific ``target`` number. Let these two numbers be
    ``numbers[index_1]`` and ``numbers[index_2]`` where
    ``1 <= index_1 < index_2 <= numbers.length``.

    Return the indices of the two numbers, ``index_1`` and
    ``index_2``, **added by one** as an integer array
    ``[index_1, index_2]`` of length 2.

    ------

    :Example 1:

    >>> Solution0167.twoSum(numbers = [2, 7, 11, 15], target = 9)
    [1, 2]


    :Example 2:

    >>> Solution0167.twoSum(numbers = [2, 3, 4], target = 6)
    [1, 3]


    :Example 3:

    >>> Solution0167.twoSum(numbers = [-1, 0], target = -1)
    [1, 2]

    """
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        """
        Args:
            numbers (List[int]): numbers to check
            target (int): the target num
        Returns:
            List[int]: the indices of the two elements that add to target

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use two pointers, starting at both ends

            if sum of pointers is too high, move ``right`` pointer down

            if sum is too low, move ``left`` pointer up

            return ``[-1, -1]`` if nothing found

        """
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]
