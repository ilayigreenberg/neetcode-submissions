# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None: return True
        return abs(self.depth(root.right) - self.depth(root.left)) <= 1
    
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left),self.depth(root.right)) + 1
        