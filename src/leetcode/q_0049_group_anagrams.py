from typing import Optional, List, Dict
from collections import defaultdict


class Solution0049:
    """
    `Medium <https://leetcode.com/problems/group-anagrams/>`_
    ---------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= strs.length <= 10^4``
        * ``0 <= strs[i].length <= 100``
        * ``strs[i]`` consists of lowercase English letters.

    Given an array of strings ``strs``, group **the anagrams** together. You
    can return the answer in **any order**.

    An **Anagram** is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.

    ------

    :Example 1:

    >>> Solution0049.groupAnagrams(strs = ['eat','tea','tan','ate','nat','bat'])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


    :Example 2:

    >>> Solution0049.groupAnagrams(strs = [''])
    [['']]


    :Example 3:

    >>> Solution0049.groupAnagrams(strs = ['a'])
    [['a']]

    """

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Args:
            strs (List[str]): list of words to group by anagram
        Returns:
            List[List[str]]: words that are anagrams grouped together

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            use a dictionary with the key being the letter counts for each word

            for the key to be hashable, use tuple indexed to ``a = 0``, ``b = 1``,
            ``c = 3``, ...

            return the values of dictionary, which will be list of words that
            have same letter counts (are anagrams)

        """
        grouped = defaultdict(list)

        for word in strs:
            anagram = Solution0049.counter(word)
            grouped[anagram].append(word)

        return list(grouped.values())

    @staticmethod
    def counter(word: str) -> tuple:
        counts = [0] * 26

        for letter in word:
            # a = 0, b = 1, ...
            index = ord(letter.lower()) - ord('a')
            counts[index] += 1

        # hashable, immutable tuple
        return tuple(counts)
