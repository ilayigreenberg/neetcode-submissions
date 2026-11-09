# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l, i = [list1, list2], 1
        dummy = node = ListNode()

        while l[i] and l[1-i]:
            if l[i].val <= l[1-i].val:
                node.next = l[i]
                l[i] = l[i].next
            else:
                i = 1-i
            node = node.next

        node.next = list1 or list2
        return dummy.next