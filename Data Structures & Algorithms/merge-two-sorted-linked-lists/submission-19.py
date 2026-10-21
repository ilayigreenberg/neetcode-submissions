# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l, i = [list1, list2], 0
        dummy = node = ListNode()

        while l[i] and l[1-i]:
            if l[i].val <= l[1-i].val:
                node.next = l[i]
                l[i] = l[i].next
                node = node.next
            else:
                i = 1-i
            

        node.next = l[0] or l[1]
        return dummy.next