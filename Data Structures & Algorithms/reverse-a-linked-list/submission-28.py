# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if head is None or head.next is None:
           # return head
        tail = None
        rest = head

        while rest:#.next:
            tmp = rest.next
            rest.next = tail

            tail = rest
            rest = tmp
        #rest.next = tail
        return tail#rest
        
                




