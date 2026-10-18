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
        if length < 3:
            return
        mid, ptr = math.ceil(length / 2), head
      
        for i in range(mid):
            ptr = ptr.next
        end, ptr = self.reverseList(ptr), head
        
        for i in range(mid - 1):
            nxthead, nxtend = ptr.next, end.next
            ptr.next = end
            end.next = nxthead 
            ptr, end = nxthead, nxtend
        if length % 2 != 0:
	        ptr.next = None 
        #return head
        
               
                             
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        rest = head
        while rest:
            tmp = rest.next
            rest.next = tail
            tail = rest
            rest = tmp
        return tail
        