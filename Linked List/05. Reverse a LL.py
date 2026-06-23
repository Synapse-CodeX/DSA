class Solution:
    def reverseList(self, head):
        temp = head
        prev = None    
        # Traverse and reverse links
        while temp is not None:
            front = temp.next     
            temp.next = prev     
            prev = temp       
            temp = front          
            
        # prev ends up at the new head of the reversed list
        return prev
        
