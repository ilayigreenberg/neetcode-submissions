# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        ptr, length = head, 0
        while ptr:
            ptr = ptr.next
            length += 1
        groups = length // k
        # now we know when to stop the reversing
        lasthead, currhead = None, head
        prv, curr = None, head
        while groups:
            currhead = curr
            for i in range(k):
                nxt = curr.next
                curr.next = prv
                prv, curr = curr, nxt   # prv = 3 ,  curr = 4
            groups -= 1
            if not lasthead:
                head = prv
            if lasthead:
                lasthead.next = prv
            lasthead = currhead 

        lasthead.next = curr
        return head
        
            





 #   def reverseK(prv, curr, k):

    
