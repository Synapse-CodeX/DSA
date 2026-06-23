# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # If the list is empty, nothing to delete
        if not head:
            return None
            
        temp = head

        if temp.val == val:
            head = temp.next
            return head
        else:
            found = False
            prev = None
            
            # Traverse the list to find the matching node
            while temp is not None:
                if temp.val == val:
                    found = True
                    break
                prev = temp
                temp = temp.next
                
            # If found, link the previous node over the deleted node
            if found:
                prev.next = temp.next
                return head
            else:
                return head



# If head is not accessible and u need to delete any node from middle (Leetcode)

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Overwrite the current node's value with the next node's value
        node.val = node.next.val
        
        # Skip the next node
        node.next = node.next.next
