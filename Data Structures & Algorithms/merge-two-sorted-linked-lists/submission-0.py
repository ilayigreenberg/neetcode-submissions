# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = minNext(list1, list2)
        
        while curr: 
            list1, list2 = list1.next if list1 else None, list2.next if list2 else None
            curr = curr.next = minNext(list1, list2)
            

        return head

    def minNext(l1, l2):
        if not l2 and l1: return l1
        if not l1 and l2: return l2
        if not l2 and not l1: return None
        return l2 if l2.val < l1.val else l1