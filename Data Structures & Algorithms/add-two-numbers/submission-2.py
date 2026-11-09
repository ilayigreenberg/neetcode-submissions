# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pt1, pt2 = l1, l2
        carry = 0
        while pt1.next and pt2.next:
            s = pt1.val + pt2.val + carry
            pt1.val, carry = s % 10, s // 10
            pt1, ptr2 = pt1.next, pt2.next
        if pt1.next:
            pt1.next.val += carry
        elif pt2.next:
            pt2.next.val += carry
            pt1.next = pt2.next                
        else:
            if carry:
                pt1.next = ListNode(1, None)
        return l1



