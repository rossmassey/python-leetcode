from typing import Optional, List, Dict

from src.common import ListNode


class Solution0206:
    """
    `Easy <https://leetcode.com/problems/reverse-linked-list/>`_
    ------------------------------------------------------------

    .. sidebar:: Constraints

        * The number of nodes in the list is the range ``[0, 5000]``
        * ``-5000 <= Node.val <= 5000``

    Given the ``head`` of a singly linked list, reverse the list, and return
    *the reversed list*

    ------

    :Example 1:

    .. image:: https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg
       :alt: The [5, 4, 3, 2, 1] linked list

    >>> example_input = ListNode.array_to_linked_list([1,2,3,4,5])
    >>> output = Solution0206.reverseList(head = example_input)
    >>> ListNode.linked_list_to_array(output)
    [5, 4, 3, 2, 1]

    :Example 2:

    .. image:: https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg
       :alt: The [1,2] linked list

    >>> example_input = ListNode.array_to_linked_list([1,2])
    >>> output = Solution0206.reverseList(head = example_input)
    >>> ListNode.linked_list_to_array(output)
    [2, 1]

    :Example 3:

    >>> example_input = ListNode.array_to_linked_list([])
    >>> output = Solution0206.reverseList(head = example_input)
    >>> ListNode.linked_list_to_array(output)
    []

    """
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Args:
            head (Optional[ListNode]): head of the linked list
        Returns:
            Optional[ListNode]: head of reversed linked list

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            update ``next`` pointer to ``prev``, ``prev`` to ``curr``, and
            ``curr`` to what was previously ``next``

            below diagram shows first pass of reverse

            .. code-block:: none

                    prev        curr
                      |           |
                    None        ( A )  -->  ( B )  -->  ( C )  --> ... None


                1. save next node in temporary variable

                    prev        curr        temp
                      |           |           |
                    None        ( A )  -->  ( B )  -->  ( C )  --> ... None


                2. set curr.next to previous node

                    prev        curr        temp
                      |           |           |
                    None   <--  ( A )       ( B )  -->  ( C )  --> ... None


                3. set prev to curr

                                prev
                                curr        temp
                                  |           |
                    None   <--  ( A )       ( B )  -->  ( C )  --> ... None


                3. set curr to temp

                                            curr
                                prev        temp
                                  |           |
                    None   <--  ( A )       ( B )  -->  ( C )  --> ... None

        """
        
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

