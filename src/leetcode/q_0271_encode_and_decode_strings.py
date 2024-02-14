from typing import Optional, List, Dict

class Solution0271:
    """
    `Medium <https://leetcode.com/problems/encode-and-decode-strings/>`_
    --------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= strs.length <= 200``
        * ``0 <= strs[i].length <= 200``
        * ``strs[i]`` contains any possible characters out of ``256`` valid ASCII characters.

    Design an algorithm to encode **a list of strings** to **a string**.
    The encoded string is then sent over the network and is decoded back to
    the original list of strings.

    Implement the ``encode`` and ``decode`` methods.

    You are not allowed to solve the problem using any serialize methods
    (such as ``eval``).

    ------

    :Example 1:

    >>> msg = ["Hello","World","Good, day! /:)"]
    >>> encoded = Solution0271.encode(msg)
    >>> Solution0271.decode(encoded) == msg
    True

    :Example 2:

    >>> msg = [""]
    >>> encoded = Solution0271.encode(msg)
    >>> Solution0271.decode(encoded) == msg
    True

    :Example (Alternative):

    >>> msg = ["{'a': [(5,1)]}", "<html>", "/../.."]
    >>> encoded = Solution0271.encode_alternative(msg)
    >>> Solution0271.decode_alternative(encoded) == msg
    True

    """
    @staticmethod
    def encode(strs: List[str]) -> str:
        """
        Args:
            strs (List[str]): strings to encode
        Returns:
            str: encoded string

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            encode the length of each ``word`` in ``strs`` as a single
            ``chr()`` prefixed to the ``word`` itself

            concatenate everything together to return as a single ``encoded``
            string

        """
        encoded = ''
        for word in strs:
            encoded += chr(len(word))
            encoded += word
        
        return encoded
        
    @staticmethod
    def decode(s: str) -> List[str]:
        """
        Args:
            s (str): encoded string
        Returns:
            List[str]: the original decoded strings

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            convert the first character to its `Unicode` code point using
            ``ord()``, which will be the ``length`` of the following string

            (the maximum length of each string below ``ord()`` upper bound)

            ``slice()`` a chunk of that ``length`` from that part of the string and
            ``append()`` to the output array ``decoded``

        """
        decoded = []
        
        i = 0
        while i < len(s):
            # first character encodes length of string
            length = ord(s[i])
            i += 1

            # slice string of corresponding length
            decoded.append(s[i:i + length])
            i += length
        
        return decoded

    @staticmethod
    def encode_alternative(strs: List[str]) -> str:
        """
        Args:
            strs (List[str]): strings to encode
        Returns:
            str: encoded string

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            since the characters in the input are in `256 ASCII`, can
            just use a `non-ASCII` character as a delimiter

            e.g. 好, 😊, π, ą, 𝕽

            use the built-in ``join()`` function

        """
        return '∞'.join(strs)

    @staticmethod
    def decode_alternative(s: str) -> List[str]:
        """
        Args:
            s (str): encoded string
        Returns:
            List[str]: the original decoded strings

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use the built-in ``split()`` function on the delimiter used
            in ``encode_alternative()``

        """
        return s.split('∞')
