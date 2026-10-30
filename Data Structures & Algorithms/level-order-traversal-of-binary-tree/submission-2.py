# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:  return []

        res, level, newlevel, newlevelVal = [[root.val]], [root], [], []

        while level:
            for node in level:
                if node.left:
                    newlevel.append(node.left)
                    newlevelVal.append(node.left.val)
                if node.right:
                    newlevel.append(node.right)
                    newlevelVal.append(node.right.val)

            if newlevelVal:  res.append(newlevelVal)
            level, newlevel, newlevelVal = newlevel, [], []
            
        
        return res