from typing import Optional, List, Dict

class Solution0347:
    """
    `Medium <https://leetcode.com/problems/top-k-frequent-elements/>`_
    ------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= nums.length <= 10^5``
        * ``-10^4 <= nums[i] <= 10^4``
        * ``k`` is in the range ``[1, the number of unique elements in the array]``.
        * It is **guaranteed** that the answer is **unique**.

    Given an integer array ``nums`` and an integer ``k``, return *the* ``k``
    *most frequent elements*. You may return the answer in **any order**.

    ------

    :Example 1:

    >>> Solution0347.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
    [1, 2]


    :Example 2:

    >>> Solution0347.topKFrequent(nums = [1], k = 1)
    [1]

    """
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """
        Args:
            nums (List[int]): nums to search
            k (int): how many to return
        Returns:
            List[int]: the k top elements

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            store all the ``num`` frequencies in a dictionary

            use bucket sort to place each number at index of its count

            return ``k`` highest nums in buckets

        """
        
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            buckets[count].append(num)
        
        # put all the nums in flat array from biggest to smallest
        flat_buckets = [num 
                        for bucket in reversed(buckets) 
                        for num in bucket]
        
        # return up to k elements
        return flat_buckets[:k]
