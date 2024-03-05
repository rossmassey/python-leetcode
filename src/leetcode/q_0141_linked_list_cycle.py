from typing import Optional, List, Dict

from src.common import ListNode

class Solution0141:
    """
    `Easy <https://leetcode.com/problems/linked-list-cycle/>`_
    ----------------------------------------------------------

    .. sidebar:: Constraints

        * The number of the nodes in the list is in the range ``[0, 10^4]``.
        * ``-10^5 <= Node.val <= 10^5``
        * ``pos`` is ``-1`` or a **valid index** in the linked-list.

    Given ``head``, the head of a linked list, determine if the linked list has
    a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can
    be reached again by continuously following the ``next`` pointer. Internally,
    ``pos`` is used to denote the index of the node that tail's ``next`` pointer
    is connected to. **Note that ``pos`` is not passed as a parameter**.

    Return ``True``* if there is a cycle in the linked list*. Otherwise, return
    ``False``.

    ------

    :Example 1:

    .. image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
       :alt: The [3,2,0,-4] linked list

    >>> example_input = ListNode.array_to_linked_list([3,2,0,-4])
    >>> nodes = example_input.get_node_objects()
    >>> nodes[-1].next = nodes[1]  # create cycle from tail to second node
    >>> Solution0141.hasCycle(head = example_input)
    True

    There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


    :Example 2:

    .. image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
       :alt: The [1,2] linked list

    >>> example_input = ListNode.array_to_linked_list([1,2])
    >>> nodes = example_input.get_node_objects()
    >>> nodes[-1].next = nodes[0]  # create cycle from tail to first node
    >>> Solution0141.hasCycle(head = example_input)
    True

    There is a cycle in the linked list, where the tail connects to the 0th node.


    :Example 3:

    .. image:: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png
       :alt: The [1,2] linked list

    >>> example_input = ListNode.array_to_linked_list([1])
    >>> nodes = example_input.get_node_objects()
    >>> Solution0141.hasCycle(head = example_input)
    False

    There is no cycle in the linked list.

    """
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        """
        Args:
            head (Optional[ListNode]): head of a linked list
        Returns:
            bool: if there is a cycle

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use floyd's cycle detection algorithm

            initialize a ``fast`` and ``slow`` pointer at the head

            while ``fast.next`` is not ``None`` (which would indicate an end of
            the list and no cycle), move ``fast`` 2 places forwards and move
            ``slow`` 1 place forward

            if ``fast`` and ``slow`` are pointing to the same object, there is
            a cycle

            else the loop will end once ``fast`` reaches it in ``O(n/2)`` time

        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
                
        return False

