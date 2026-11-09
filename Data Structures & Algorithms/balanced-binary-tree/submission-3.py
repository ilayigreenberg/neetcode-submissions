# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        q = deque([root]) if root else None
        level = 0
        leafLevel, con = 0, False

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not (con or node.left and node.right):
                    leafLevel = level + 1
                    con = True
            level += 1
            if con and level - leafLevel > 1:
                return False

        return True
        