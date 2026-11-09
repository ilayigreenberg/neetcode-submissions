# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        import math

        length, ptr = 0, head
        while ptr:
            length += 1
            ptr = ptr.next
        mid, ptr = math.ceil(length / 2) - 1, head
      
        while mid:
            ptr = ptr.next
            mid -= 1
        #separating the end of the head list from the rest
        tmp = ptr.next
        ptr.next = None
        end, ptr = self.reverseList(tmp), head
        
        while ptr:
            nxthead = ptr.next
            ptr.next = end
            
            nxtend = end.next
            end.next = nxthead 
            
            ptr = nxthead
            end = nxtend
         
        return head
        
               
                             
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        rest = head
        while rest:
            tmp = rest.next
            rest.next = tail
            tail = rest
            rest = tmp
        return tail
        