# Definition for singly-linked list.
class ListNode:
    """
    Leetcode provided ListNode class

    Represents a node in a linked list
    """
    def __init__(self, val=0, next=None):
        """
        Creates a ListNode

        Args:
            val (int): node value
            next (ListNode): next node)

        Returns:
            ListNode: the node
        """
        self.val = val
        self.next = next
