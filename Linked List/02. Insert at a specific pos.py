# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert_at(self, val: int, position: int) -> list[int]:
        """
        Inserts a new node with the given value at the specified position
        and returns the full updated list elements as an array.
        """
        new_node = ListNode(val)
        
        # Case 1: Insertion at the beginning (position 0)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Case 2: Insertion at any other position
            current = self.head
            prev_node = None
            count = 0
            
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            
            # Link the new node into the list
            prev_node.next = new_node
            new_node.next = current

        # Traverse and return the updated list elements
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.val)
            curr = curr.next
        return elements
