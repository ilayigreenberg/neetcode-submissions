# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and head.next:
            rest = self.reverseList(head.next)
            head.next = None
            rest.next = head
            return rest
        return head
        
        
        
        
        
        
        
        """if head and head.next:
            rest = head.next
            self.reverseList(rest)
            rest.next = head
        return head"""


        
        
         