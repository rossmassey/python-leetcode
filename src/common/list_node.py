from __future__ import annotations  # can reference this class in itself

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

    # HELPER METHODS (not provided by leetcode)
    def get_node_objects(self) -> list:
        """
        Gets an array with access to all the nodes, treating
        current node as the head (index ``0``)

        Returns:
            list: list of all the node objects
        """
        index = []
        node = self
        while node:
            index.append(node)
            node = node.next

        return index

    @staticmethod
    def array_to_linked_list(linked_list: list) -> ListNode:
        """
        Converts an array to a linked list.

        Args:
            linked_list (List[int]): array to convert

        Returns:
            ListNode: head of the linked list
        """
        if not linked_list:
            return None

        head = ListNode(linked_list[0])
        current = head

        for value in linked_list[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

    @staticmethod
    def linked_list_to_array(head: ListNode) -> list:
        """
        Converts a linked list to an array

        Args:
            head (ListNode): head of the linked list

        Returns:
            List[int]: array representation of the linked list
        """
        linked_list = []
        current = head

        while current:
            linked_list.append(current.val)
            current = current.next

        return linked_list
