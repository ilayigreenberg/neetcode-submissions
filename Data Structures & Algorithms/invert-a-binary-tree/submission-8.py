# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        level, newlevel = [root] if root else [], []
        while level:
            for n in level:
                if not n:   continue
                n.left, n.right = n.right, n.left
                if n.left:  newlevel.append(n.left)
                if n.right:  newlevel.append(n.right)

                level, newlevel = newlevel, []
        return root