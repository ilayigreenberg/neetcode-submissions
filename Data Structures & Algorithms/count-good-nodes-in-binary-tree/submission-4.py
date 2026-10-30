# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([[root, root.val]])
        res = 1
        while q:
            node, biggest = q.popleft()
            sons = [node.left, node.right]

            for son in sons:
                if son:
                    if son.val >= biggest:
                        res += 1
                    q.append([son, max(biggest, son.val)])

        return res