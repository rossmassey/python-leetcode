from typing import Optional, List, Dict

class Solution0150:
    """
    `Medium <https://leetcode.com/problems/evaluate-reverse-polish-notation/>`_
    ---------------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= tokens.length <= 10^4``
        * ``tokens[i]`` is either an operator: ``"+"``, ``"-"``, ``"*"``, or ``"/"``, or an integer in the range ``[-200, 200]``.

    You are given an array of strings ``tokens`` that represents an arithmetic
    expression in `Reverse Polish Notation <https://en.wikipedia.org/wiki/Reverse_Polish_notation>`_

    Evaluate the expression. Return *an integer that represents the value of
    the expression*.

    **Note** that:

    * The valid operators are ``'+'``, ``'-'``, ``'*'``, and ``'/'``.
    * Each operand may be an integer or another expression.
    * The division between two integers always **truncates toward zero**.
    * There will not be any division by zero.
    * The input represents a valid arithmetic expression in a reverse polish notation.
    * The answer and all the intermediate calculations can be represented in a **32-bit** integer.

    ------

    :Example 1:

    >>> Solution0150.evalRPN(tokens = ["2","1","+","3","*"])
    9

    * ((2 + 1) * 3) = 9


    :Example 2:

    >>> Solution0150.evalRPN(tokens = ["4","13","5","/","+"])
    6

    * (4 + (13 / 5)) = 6


    :Example 3:

    >>> Solution0150.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    22


    * ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    * = ((10 * (6 / (12 * -11))) + 17) + 5
    * = ((10 * (6 / -132)) + 17) + 5
    * = ((10 * 0) + 17) + 5
    * = (0 + 17) + 5
    * = 17 + 5
    * = 22

    """
    @staticmethod
    def evalRPN(tokens: List[str]) -> int:
        """
        Args:
            tokens (List[str]): RPN input
        Returns:
            int: result of operations

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            create a dictionary ``ops`` that contain all the operations mapped
            to lambda functions

            use ``stack`` to track inputs and intermediary results

            if ``token`` not in ``ops``, just add to ``stack``

            else, pop the last two elements in the ``stack`` and apply op

            return final element in ``stack``

        """
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }
        
        stack = []

        for token in tokens:
            if token in ops:
                y = int(stack.pop())  # most recent on stack is second operand
                x = int(stack.pop())  # then first operand

                stack.append(ops[token](x, y))
            else:
                stack.append(token)
        
        return int(stack.pop())
