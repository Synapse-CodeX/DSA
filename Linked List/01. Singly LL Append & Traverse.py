# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def append(self, val: int) -> None:
        """
        Appends a new node with the given value to the end of the linked list.
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def traverse(self) -> list[int]:
        """
        Traverses the linked list and returns all elements as a list.
        """
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.val)
            current = current.next
        return elements
