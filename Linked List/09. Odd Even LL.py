# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         # self.val = val
#         # self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        even_head = even  # Remember the start of the even list to connect later
        
        # Rearrange nodes
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
            
        # Connect the end of the odd list to the head of the even list
        odd.next = even_head
        
        return head
