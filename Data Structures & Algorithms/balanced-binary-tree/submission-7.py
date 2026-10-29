# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root):
        stack = [[root, -1, -1]] if root else []

        while stack:
            curr, prv = stack[-1], stack[-2] if len(stack) > 1 else None
            node, prvNode = curr[0], prv[0] if prv else None
            # curr full depth is set then updating his father depth part
            if curr[1] >= 0 or curr[2] >= 0:
                if curr[1] < 0: curr[1] = 0
                elif curr[2] < 0: curr[2] = 0
                if abs(curr[1] - curr[2]) > 1:
                    return False
                if len(stack) == 1:
                    return True
                # matching prv to curr's father
                if not (prvNode.right is node or prvNode.left is node):
                    prv = stack[-3]
                i = 2 if prv[1] >= 0 else 1
                prv[i] = 1 + max(curr[1], curr[2])
                stack.pop()
                continue
            # even is curr has just one depth val, we'll take care of his other son before seeing him again so we won't get here
            left, right = node.left, node.right
            if left: stack.append([left, -1, -1])
            if right: stack.append([right, -1, -1])

            if not (left or right):
                curr[1], curr[2] = 0, 0
            # letting the while iterate again with full depth curr
#but then we will update only one of the father fields
               # if prvNode.right is node or prvNode.left is node:
               #     prv[1] = 0


        return True



