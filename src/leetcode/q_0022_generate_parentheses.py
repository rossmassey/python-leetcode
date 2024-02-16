from typing import Optional, List, Dict

class Solution0022:
    """
    `Medium <https://leetcode.com/problems/generate-parentheses/>`_
    ---------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= n <= 8``

    Given ``n`` pairs of parentheses, write a function to *generate all
    combinations of well-formed parentheses*.

    ------

    :Example 1:

    >>> Solution0022.generateParenthesis(n = 3)
    ['()()()', '()(())', '(())()', '(()())', '((()))']


    :Example 2:

    >>> Solution0022.generateParenthesis(n = 1)
    ['()']

    """
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        """
        Args:
            n (int): how many parentheses
        Returns:
            List[str]: valid combinations of parentheses

        ------

        :Runtime:   ``O(4^n / (n^(3/2)))`` (bigger than ``O(2^n)``)
        :Space:     ``O(4^n / (n^(3/2)))``

        :Strategy:

            use a ``stack`` to track partial strings which have not used all
            parentheses available yet, popping until it is empty (start with
            empty string)

            track number of ``open_parens`` and ``close_parens``, add a ``'('``
            and ``')'`` to the partial string if it will remain valid, and add
            to ``stack``

            once the partial string is at length ``2n``, it will have
            ``open_parens == close_parens == n``

            the number of valid parentheses generated is the ``n`` Catalan
            number, which grows exponentially at ``4^n / (n^(3/2))``

        :Alternative:

            can use recursion instead of a stack, with backtracking

        """
        result = []

        if n <= 0:
            return result

        # use stack instead of recursive calls
        stack = [([], 0, 0)]

        while stack:
            partial, open_parens, close_parens = stack.pop()

            # each valid combination is 2n in length
            if len(partial) == 2 * n:
                result.append(''.join(partial))

            # consider partial string ending with '(' if some available
            if open_parens < n:
                stack.append((partial + ['('], open_parens + 1, close_parens))

            # consider partial string ending with ')' if able to close some open ones
            if close_parens < open_parens:
                stack.append((partial + [')'], open_parens, close_parens + 1))

        return result
