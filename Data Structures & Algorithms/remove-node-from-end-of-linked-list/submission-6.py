# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, ptr = 0, head
        while ptr:
            ptr = ptr.next
            length += 1
        m, ptr = length - n - 1, head
        if m < 0:
            return head.next
        while m > 0:
            ptr = ptr.next
            m -= 1
        ptr.next = ptr.next.next if ptr.next else None
        
        return head





        