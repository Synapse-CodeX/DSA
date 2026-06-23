# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        # Phase 1: Determine if a cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle is detected
            if slow == fast:
                # Phase 2: Find the starting point of the cycle
                slow = head  # Reset slow to head 
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next  # Both move 1 step now
                    
                return slow  # Both pointers meet at the starting node
                
        # If fast reaches the end, there is no loop
        return None
