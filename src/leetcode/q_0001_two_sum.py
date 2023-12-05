from typing import List, Dict

"""
[Two Sum](https://leetcode.com/problems/two-sum/) - Easy

Given an array of integers ``nums`` and an integer ``target``, return indices of
the two numbers such that they add up to ``target``.

You may assume that each input would have **exactly one solution**, and you may
not use the same element twice. You can return the answer in any order.

Constraints:
- ``2 <= len(nums) <= 10^4``
- ``-10^9 <= nums[i] <= 10^9``
- ``-10^9 <= target <= 10^9``
- Only one valid answer exists.
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Runtime:    ``O(n)``
    Space:      ``O(n)``

    use a dictionary ``indexOfComplements`` to store potential complements
    (difference of ``target`` and current ``num``) and their indices

    iterate over ``nums``, if current ``num`` is found in the dictionary,
    return its ``index`` along with the ``otherIndex`` from the dictionary,
    which will be two indices whose elements add up to the ``target``

    :rtype: object
    :param nums: List of integers.
    :param target: The target sum.
    :return: Indices of the two numbers that add up to the target.
    """
    index_of_complements: Dict[int, int] = {}

    for index, num in enumerate(nums):
        if num in index_of_complements:
            return [index, index_of_complements[num]]
        index_of_complements[target - num] = index

    return [-1, -1]
