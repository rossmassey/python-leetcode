from typing import Optional, List, Dict

class Solution0128:
    """
    `Medium <https://leetcode.com/problems/longest-consecutive-sequence/>`_
    -----------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``0 <= nums.length <= 10^5``
        * ``-10^9 <= nums[i] <= 10^9``

    Given an unsorted array of integers ``nums``, return *the length of the
    longest consecutive elements sequence.*

    You must write an algorithm that runs in ``O(n)`` time.

    ------

    :Example 1:

    >>> Solution0128.longestConsecutive(nums = [100,4,200,1,3,2])
    4

    The longest consecutive elements sequence is ``[1, 2, 3, 4]``. Therefore its length is 4.


    :Example 2:

    >>> Solution0128.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
    9


    """
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): nums to search
        Returns:
            int: length of the longest consecutive sequence

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            use a ``set`` or ``dict`` to index all the ``nums``

            for each ``num``, count how many times it can go forward ``num + 1``
            and have the next element of the sequence available

            if ``num - 1`` is present, skip counting to avoid duplicate work
            and only start from beginning of sequences

            track the ``max()`` sequence length and return it

        """
        
        longest_sequence = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) in num_set:
                continue

            current_sequence = 1
            current = num

            while (current + 1) in num_set:
                current_sequence += 1
                current += 1
            
            longest_sequence = max(current_sequence, longest_sequence)
            
        return longest_sequence
