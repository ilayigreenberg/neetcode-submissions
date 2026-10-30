# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        stack = [root]
        i, j = 1, 0
        while i:
            for i in range(len(stack) - 1, len(stack) - 1 - i, -1):
                node = stack[i]
                if node.left:
                    stack.append(node.left)
                    j += 1
                if node.right:
                    stack.append(node.right)
                    j += 1
                i, j = j, 0

        seen, maxDiameter =  {}, 0
        while stack:
            node = stack.pop()

            depth = 1 + max(seen[node.left][0] if node.left in seen else 0, 
                            seen[node.right][0] if node.right in seen else 0)
            if not node.left and not node.right: depth = 0
            diameter = (2 + (seen[node.left][0] if node.left in seen else -1) 
                          + (seen[node.right][0] if node.right in seen else -1))

            seen[node] = [depth, diameter]
            maxDiameter = max(maxDiameter, diameter)
        
        return maxDiameter




