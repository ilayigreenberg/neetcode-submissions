# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root: return []
        level, res = [root], [root.val]
        newlevel, done = [], False

        while level:
            for node in level:
                if not done and node.right:
                    res.append(node.right.val)
                    done = True
                if not done and node.left:
                    res.append(node.left.val)
                    done = True

                if node.right: newlevel.append(node.right)
                if node.left: newlevel.append(node.left)

            level, newlevel = newlevel, []
            done = False
        
        return res