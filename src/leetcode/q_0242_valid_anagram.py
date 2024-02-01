from typing import Optional, List, Dict

class Solution0242:
    """
    `Easy <https://leetcode.com/problems/valid-anagram/>`_
    ------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= s.length, t.length <= 5 * 10^4``
        * ``s`` and ``t`` consist of lowercase English letters.

    Given two strings ``s`` and ``t``, return ``True`` *if* ``t`` *is an
    anagram of* ``s``*, and* ``False`` *otherwise*.

    An **Anagram** is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.

    ------

    :Example 1:

    >>> Solution0242.isAnagram(s = "anagram", t = "nagaram")
    True


    :Example 2:

    >>> Solution0242.isAnagram(s = "rat", t = "car")
    False

    """
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """
        Args:
            s (str): source string
            t (str): string to check
        Returns:
            bool: if ``t`` is an anagram of ``s``

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            two strings are anagrams if they have the same count for each
            letter

            create dictionary mapping letter to frequency for both strings,
            compare for equivalence

        """
        return Solution0242.counter(s) == Solution0242.counter(t)

    # simple version of collections.Counter
    @staticmethod
    def counter(s):
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        return letters
