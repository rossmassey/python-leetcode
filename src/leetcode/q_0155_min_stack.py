class Solution0155:
    """
    `Medium <https://leetcode.com/problems/min-stack/>`_
    ----------------------------------------------------

    .. sidebar:: Constraints

        * ``-2^31 <= val <= 2^31 - 1``
        * Methods ``pop``, ``top`` and ``getMin`` operations will always be called on non-empty stacks.
        * At most ``3 * 10^4`` calls will be made to ``push``, ``pop``, ``top``, and ``getMin``.

    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

        * ``MinStack()`` initializes the stack object.
        * ``void push(int val)`` pushes the element val onto the stack.
        * ``void pop()`` removes the element on the top of the stack.
        * ``int top()`` gets the top element of the stack.
        * ``int getMin()`` retrieves the minimum element in the stack.

    You must implement a solution with ``O(1)`` time complexity for each function.

    ------

    :Example 1:

    >>> minStack = Solution0155()
    >>> minStack.push(-2)
    >>> minStack.push(0)
    >>> minStack.push(-3)
    >>> minStack.getMin()
    -3
    >>> minStack.pop()
    >>> minStack.top()
    0
    >>> minStack.getMin()
    -2

    """
    def __init__(self):
        """
        :Strategy:

            use two stacks, one for the elements and one for the ``mins``

            when pushing to the MinStack, check if the value is less than or
            equal to one at top of the ``mins``, and track new min. this
            may be a duplicate of the previous min

            when popping, the ``mins`` stack is only popped if it matches
            the value being popped (duplicates handled by ``mins`` also having
            duplicates)

        :Alternative:

            * use one stack with pairs (the value and the current min at that point)
            * use two stacks, but track number of repeated mins instead of duplicating

        """
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        """
        Push a value to the stack

        Args:
            val (int): value to push onto stack

        ------

        :Runtime:   ``O(1)``
        :Space:     ``O(1)``

        """
        self.stack.append(val)

        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        """
        Pop a value from the stack

        :Runtime:   ``O(1)``
        :Space:     ``O(1)``

        """
        if self.mins[-1] == self.stack[-1]:
            self.mins.pop()

        self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack

        Returns:
            int: the value at the top of the stack

        ------

        :Runtime:   ``O(1)``
        :Space:     ``O(1)``

        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Get the minimum element in the stack

        Returns:
            int: the minimum value in the stack

        ------

        :Runtime:   ``O(1)``
        :Space:     ``O(1)``

        """
        return self.mins[-1]
