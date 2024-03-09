from collections import defaultdict

class Solution0424:
    """
    `Medium <https://leetcode.com/problems/longest-repeating-character-replacement/description/>`_
    ----------------------------------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= s.length <= 10^5``
        * ``s`` consists of only uppercase English letters.
        * ``0 <= k <= s.length``

    You are given a string ``s`` and an integer ``k``. You can choose any
    character of the string and change it to any other uppercase English
    character. You can perform this operation at most ``k`` times.

    Return the length of the longest substring containing the same letter you
    can get after performing the above operations.

    ------

    :Example 1:

    >>> Solution0424.characterReplacement(s = "ABAB", k = 2)
    4

    Replace the two 'A's with two 'B's or vice versa.

    :Example 2:

    >>> Solution0424.characterReplacement(s = "AABABBA", k = 1)
    4

    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.

    """
    @staticmethod
    def characterReplacement(s: str, k: int) -> int:
        """
        Args:
            s (str): string to check
            k (int): max number of replacements
        Returns:
            int: longest single-character substring after up to k replacements

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``, only need to store 'A-Z' counts (at most 26)

        :Strategy:

            use a sliding window with ``start`` and ``end`` (current) character,
            starting with single character at the beginning

            keep frequency ``counts`` of all the characters in the window

            find the ``most_frequent`` character in each window to minimize number
            of characters needing replacement. there are only 'A-Z' possible
            keys, so it is ``O(26) = O(1)`` operation

            valid window will have condition ``length - most_frequent <= k``,
            since that means it can be changed to uniform characters (see below)

            if window is not valid, move ``start`` forward to decrease the
            window size, updating the character frequencies as they are dropped

            for each valid window, check against ``longest_substring`` seen so far

            **Note about the condition:**

            if :math:`X` is most frequent character, want to replace everything
            that is :math:`\\neq X`

            ex) :math:`AXXBXC=\\text{Not Valid}`

            need ``k`` or less of the non most frequent characters to be able to
            change them all to create a valid string

            ex) :math:`\\hat{X}XX\\hat{X}X\\hat{X}=\\text{Valid } (k \\leq 3)`

            if more than ``k`` of the non-most frequent character are
            introduced, shift ``start`` forward until condition valid again

            .. code-block:: none

                AXXBXCC        AXXBXCC        AXXBXCC
                ^    ^    ->   ^     ^   ->    ^    ^
                s    e         s     e         s    e

                (valid)        (invalid)      (valid)

        """
        counts = defaultdict(int)  # default is 0
        longest_substring = 0
        start = 0

        for end, character in enumerate(s):
            counts[character] += 1

            most_frequent = max(counts.values())  # only 'A-Z' to check
            substring_length = end - start + 1

            # if condition valid with overestimated most_frequent, it is valid
            # for actual most_frequent. can avoid recomputing
            while substring_length - most_frequent > k:
                counts[s[start]] -= 1
                start += 1
                substring_length -= 1

            longest_substring = max(longest_substring, substring_length)

        return longest_substring
