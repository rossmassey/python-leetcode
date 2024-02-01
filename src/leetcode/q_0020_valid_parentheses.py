from typing import Optional, List, Dict

class Solution0020:
    """
    `Easy <https://leetcode.com/problems/valid-parentheses/>`_
    ----------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= s.length <= 10^4``
        * ``s`` consists of parentheses only ``'()[]{}'``.

    Given a string ``s`` containing just the characters ``'('``, ``')'``,
    ``'{'``, ``'}'``, ``'['`` and ``']'``, determine if the input string is
    valid.

    An input string is valid if:

    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.

    ------

    :Example 1:

    >>> Solution0020.isValid(s = "()")
    True


    :Example 2:

    >>> Solution0020.isValid(s = "()[]{}")
    True


    :Example 3:

    >>> Solution0020.isValid(s = "(]")
    False

    """
    @staticmethod
    def isValid(s: str) -> bool:
        """
        Args:
            s (str): string with braces
        Returns:
            bool: if all opening braces are closed properly

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            add opening braces to a stack

            when a closing brace encountered, pop from stack if top matches
            (i.e. ``'('`` on top of stack will be popped if ``')'`` is found)

            if the stack is not empty at the end, not all braces were matched
            in correct order

        """
        # must be even length string
        if len(s) % 2 != 0:
            return False

        pairs = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }

        stack = []

        for brace in s:
            # last opening brace can be closed by first matching closing brace
            if stack and brace in pairs and pairs[brace] == stack[-1]:
                stack.pop()
            # if not closing a brace, add to stack
            else:
                stack.append(brace)

        # if the stack is not empty, not all braces matched
        return not stack

