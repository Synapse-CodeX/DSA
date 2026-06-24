# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # If fast reaches None, it means we need to remove the head node
        if fast is None:
            return head.next
            
        # Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        # Delete the N-th node from the end
        slow.next = slow.next.next
        
        return head
        
