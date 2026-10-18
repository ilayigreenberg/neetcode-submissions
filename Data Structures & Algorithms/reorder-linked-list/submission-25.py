# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        length, ptr = 0, head
        while ptr:
            length += 1
            ptr = ptr.next
        mid, ptr = math.ceil(length / 2), head
      
        for i in range(mid - 1):
            ptr = ptr.next
        end, p = self.reverseList(ptr.next), head
        ptr.next = None
        
        while end:
            nxthead, nxtend = p.next, end.next
            p.next = end
            end.next = nxthead 
            p, end = nxthead, nxtend
 
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
        