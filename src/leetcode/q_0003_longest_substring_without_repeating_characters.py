from typing import Optional, List, Dict

class Solution0003:
    """
    `Medium <https://leetcode.com/problems/longest-substring-without-repeating-characters/>`_
    -----------------------------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``0 <= s.length <= 5 * 10^4``
        * ``s`` consists of English letters, digits, symbols and spaces.

    Given a string ``s``, find the length of the **longest substring** without
    repeating characters.

    ------

    :Example 1:

    >>> Solution0003.lengthOfLongestSubstring(s = "abcabcbb")
    3

    The answer is "abc", with the length of 3.


    :Example 2:

    >>> Solution0003.lengthOfLongestSubstring(s = "bbbbb")
    1

    The answer is "b", with the length of 1.


    :Example 3:

    >>> Solution0003.lengthOfLongestSubstring(s = "pwwkew")
    3

    The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    """
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        Args:
            s (str): string of letters
        Returns:
            int: longest substring of unique letters

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            use a dictionary ``seen`` to track the most recent index of each
            unique letter

            track start of current substring (of unique letters) and longest
            length seen

            iterate through ``s``, for each ``letter`` check if had been seen
            already, reset ``substring_start`` to be position after the last
            seen (to maintain rolling window of unique letters)

            return ``longest_length`` seen

        """
        
        longest_length = 0
        substring_start = 0

        seen = {}

        for (i, letter) in enumerate(s):
            last_seen = seen.get(letter)

            if last_seen is not None and last_seen >= substring_start:
                substring_start = last_seen + 1

            current_length = i - substring_start + 1
            longest_length = max(longest_length, current_length)

            seen[letter] = i
        
        return longest_length
