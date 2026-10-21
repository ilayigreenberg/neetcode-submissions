# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l = [None, list1, list2]
        if not l[1]:    return l[2]
        if not l[2]:    return l[1]
        i = 1 if l[1].val <= l[2].val else 2
        curr = l[0] = l[i]
        while True:
            while curr.next and curr.next.val <= l[3-i].val:
                curr = curr.next
            if not curr.next:   # while iterating we've reach the end of that list
                curr.next = l[3-i]
                return l[0]    
            # update node of current list to his next before moving iterate the other list
            l[i] = curr.next
            # update curr to the node of the other list
            curr.next = l[3-i]
            curr = l[3-i]
            i = 3-i
        
            

                