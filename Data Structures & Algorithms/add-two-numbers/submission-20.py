# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        pt1, pt2 = l1, l2
        carry, dummy = 0, ListNode(0, None)
        while True:
            s = pt1.val + pt2.val + carry
            pt1.val, carry = s % 10, s // 10
            if pt1.next:
                pt1, pt2 = pt1.next, pt2.next if pt2.next else dummy
                continue
            # if l2 is larger we swapping
            if pt2.next:
                pt1.next, pt2 = pt2.next, dummy
                pt1 = pt1.next
                continue
                
            if carry:
                pt1.next = ListNode(1, None)
            return l1
          



