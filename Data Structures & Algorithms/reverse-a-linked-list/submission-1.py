# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while True:
            second = head.next
            third = second.next
            second.next = head

            head = second
            second = third
            if not second:
                break
        return head