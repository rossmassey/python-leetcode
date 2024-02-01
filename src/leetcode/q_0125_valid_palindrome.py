from typing import Optional, List, Dict

class Solution0125:
    """
    `Easy <https://leetcode.com/problems/valid-palindrome/>`_
    ---------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= s.length <= 2 * 10^5``
        * ``s`` consists only of printable ASCII characters.

    A phrase is a **palindrome** if, after converting all uppercase letters
    into lowercase letters and removing all non-alphanumeric characters, it
    reads the same forward and backward. Alphanumeric characters include
    letters and numbers.

    Given a string ``s``, return ``True`` *if it is a **palindrome**, or
    *``False``* otherwise*.

    ------

    :Example 1:

    >>> Solution0125.isPalindrome(s = "A man, a plan, a canal: Panama")
    True

    "amanaplanacanalpanama" is a palindrome.


    :Example 2:

    >>> Solution0125.isPalindrome(s = "race a car")
    False

    "raceacar" is not a palindrome.


    :Example 3:

    >>> Solution0125.isPalindrome(s = " ")
    True

    s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a
    palindrome.

    """
    @staticmethod
    def isPalindrome(s: str) -> bool:
        """
        Args:
            s (str): string to check
        Returns:
            bool: if it is a palindrome

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            filter for alphanumeric letters and lowercase

            use two pointers checking from both ends that letters match

            converge towards middle while ``left`` less than ``right``

        """
        letters = [letter.lower() for letter in s if letter.isalnum()]

        left = 0
        right = len(letters) - 1
        while left < right:
            if letters[left] != letters[right]:
                return False
            
            left += 1
            right -= 1
        
        return True


