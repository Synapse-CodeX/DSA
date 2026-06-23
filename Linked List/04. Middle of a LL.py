# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        # Initialize both pointers to the head of the list
        slow = head
        fast = head
        
        # Traverse the list: fast moves 2 steps, slow moves 1 step
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # When fast reaches the end, slow is exactly at the middle node
        return slow
        
