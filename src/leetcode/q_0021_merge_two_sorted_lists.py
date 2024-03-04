from typing import Optional, List, Dict

from src.common import ListNode

class Solution0021:
    """
    `Easy <https://leetcode.com/problems/merge-two-sorted-lists/>`_
    ---------------------------------------------------------------

    .. sidebar:: Constraints

        * The number of nodes in both lists is in the range ``[0, 50]``.
        * ``-100 <= Node.val <= 100``
        * Both ``list1`` and ``list2`` are sorted in **non-decreasing** order.

    You are given the heads of two sorted linked lists ``list1`` and ``list2``.

    Merge the two lists into one **sorted** list. The list should be made by
    splicing together the nodes of the first two lists.

    Return *the head of the merged linked list*.

    ------

    :Example 1:

    >>> list1 = ListNode.array_to_linked_list([1,2,4])
    >>> list2 = ListNode.array_to_linked_list([1,3,4])
    >>> output = Solution0021.mergeTwoLists(list1, list2)
    >>> ListNode.linked_list_to_array(output)
    [1, 1, 2, 3, 4, 4]


    :Example 2:

    >>> list1 = ListNode.array_to_linked_list([])
    >>> list2 = ListNode.array_to_linked_list([])
    >>> output = Solution0021.mergeTwoLists(list1, list2)
    >>> ListNode.linked_list_to_array(output)
    []


    :Example 3:

    >>> list1 = ListNode.array_to_linked_list([])
    >>> list2 = ListNode.array_to_linked_list([0])
    >>> output = Solution0021.mergeTwoLists(list1, list2)
    >>> ListNode.linked_list_to_array(output)
    [0]

    """
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Args:
            list1 (Optional[ListNode]): a sorted linked list
            list2 (Optional[ListNode]): a sorted linked list
        Returns:
            Optional[ListNode]: merged linked list in sorted order

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use a sentinel node to get back to the head easily, and an initial
            pointer ``merged`` pointing to the sentinel ``head``

            iterate through ``list1`` and ``list2`` pointers while they are both
            not ``None``

            if ``list1`` node is ``<=``, add ``merged`` and move them both
            forward. else ``list2`` node is smaller, so add that one

            append remaining nodes if any are left once ``list1`` or ``list2``
            pointer is ``None``

            return the node the sentinel ``head`` has as ``.next``

        """
        # sentinel node pointing to head
        head = ListNode(None)
        # pointer to merged list
        merged = head

        while (list1 and list2):
            if list1.val <= list2.val:
                # list1 smaller/equal, append to merged list
                merged.next = list1
                # move list1 pointer forward
                list1 = list1.next
            else:
                # else list2 smaller
                merged.next = list2
                list2 = list2.next
            
            # move merged list pointer forward
            merged = merged.next

        # one could still have remaining nodes
        merged.next = list1 if list1 else list2

        return head.next

    @staticmethod
    def mergeTwoListsRecursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Args:
            list1 (Optional[ListNode]): a sorted linked list
            list2 (Optional[ListNode]): a sorted linked list
        Returns:
            Optional[ListNode]: merged linked list in sorted order

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            recursive approach

            base case is if ``list1`` or ``list2`` is ``None``, just return
            the other one (which might be ``None``)

            if ``list1`` is smaller than ``list2``, so it will be the head of the
            current sublist

            ``list1.next`` and ``list2`` are recursively merged and appended
            to ``list1``, which is returned

            else ``list2`` is smaller (or equal), it will be the head instead

            ``list2.next`` and ``list1`` are recursively merged and appended
            to ``list2``, which is returned

        """
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            # list1 node is smaller, the rest will follow and be merged
            list1.next = Solution0021.mergeTwoListsRecursive(list1.next, list2)
            # list1 is head of the merged sublist
            return list1
        else:
            # else list2 is smaller
            list2.next = Solution0021.mergeTwoListsRecursive(list1, list2.next)
            return list2 
